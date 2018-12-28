# -*- coding: utf-8 -*-
import scrapy
import json
from scrapy import Request
# from scrapy.shell import inspect_response
from oj.items import OjItem
import time, os
import requests
import re
# import tomd


class ProblemSpider(scrapy.Spider):
    name = 'problem'
    allowed_domains = ['loj.ac']
    start_urls = ['https://loj.ac/problem']

    def parse(self, response):
        """处理问题列表"""
        # a = [10223, 10224, 10225, 10226, 10227, 10228, 10229, 10230, 10231, 10232, 10233, 10234, 10235, 10236, 10237,
        #      10238, 10239, 10240, 10241, 10242, 10243, 10244, 10245, 10246, 10247, 10248, 10249, 10173, 10174, 10175,
        #      10176, 10177, 10178, 10179, 10180, 10181, 10182, 10183, 10184, 10185, 10186, 10187, 10188, 10189, 10190,
        #      10191, 10192, 10193, 10194, 10195, 10196, 10197, 10198, 10199, 10200, 10201, 10202, 10203, 10204, 10205,
        #      10206, 10207, 10208, 10209, 10210, 10211, 10212, 10213, 10214, 10215, 10216, 10217, 10218, 10219, 10220,
        #      10221, 10222, 10123, 10124, 10125, 10126, 10127, 10128, 10129, 10130, 10131, 10132, 10133, 10134, 10135,
        #      10136, 10137, 10138, 10139, 10140, 10141, 10142, 10143, 10144, 10145, 10146, 10147, 10148, 10149, 10150,
        #      10151, 10152, 10153, 10154, 10155, 10156, 10157, 10158, 10159, 10160, 10161, 10162, 10163, 10164, 10165,
        #      10166, 10167, 10168, 10169, 10170, 10171, 10172, 10073, 10074, 10075, 10076, 10077, 10078, 10079, 10080,
        #      10081, 10082, 10083, 10084, 10085, 10086, 10087, 10088, 10089, 10090, 10091, 10092, 10093, 10094, 10095,
        #      10096, 10097, 10098, 10099, 10100, 10101, 10102, 10103, 10104, 10105, 10106, 10107, 10108, 10109, 10110,
        #      10111, 10112, 10113, 10114, 10115, 10116, 10117, 10118, 10119, 10120, 10121, 10122, 10023, 10024, 10025,
        #      10026, 10027, 10028, 10029, 10030, 10031, 10032, 10033, 10034, 10035, 10036, 10037, 10038, 10039, 10040,
        #      10041, 10042, 10043, 10044, 10045, 10046, 10047, 10048, 10049, 10050, 10051, 10052, 10053, 10054, 10055,
        #      10056, 10057, 10058, 10059, 10060, 10061, 10062, 10063, 10064, 10065, 10066, 10067, 10068, 10069, 10070,
        #      10071, 10072, 6502, 6503, 6504, 6507, 6508, 6509, 6510, 6511, 6512, 6513, 6514, 6515, 6516, 6517, 6518,
        #      6519, 6520, 6533, 6534, 6537, 6538, 6539, 6540, 6541, 6542, 6543, 6544, 10000, 10001, 10002, 10003, 10004,
        #      10005, 10006, 10007, 10008, 10009, 10010, 10011, 10012, 10013, 10014, 10015, 10016, 10017, 10018, 10019,
        #      10020, 10021, 10022, 6411, 6412, 6413, 6432, 6433, 6434, 6435, 6436, 6437, 6438, 6440, 6462, 6463, 6464,
        #      6465, 6466, 6467, 6468, 6469, 6470, 6471, 6472, 6473, 6474, 6475, 6476, 6477, 6478, 6479, 6480, 6481, 6482,
        #      6483, 6484, 6485, 6487, 6488, 6489, 6490, 6491, 6492, 6493, 6494, 6495, 6496, 6497, 6498, 6499, 6500, 6501,
        #      6360, 6361, 6362, 6363, 6365, 6366, 6367, 6368, 6369, 6370, 6371, 6372, 6373, 6374, 6375, 6376, 6377, 6378,
        #      6379, 6380, 6381, 6382, 6383, 6384, 6385, 6386, 6387, 6388, 6389, 6390, 6391, 6392, 6393, 6394, 6395, 6396,
        #      6397, 6398, 6399, 6400, 6401, 6402, 6403, 6404, 6405, 6406, 6407, 6408, 6409, 6410, 6278, 6279, 6280, 6281,
        #      6282, 6283, 6284, 6285, 6286, 6287, 6288, 6289, 6290, 6291, 6292, 6293, 6294, 6295, 6296, 6297, 6298, 6299,
        #      6300, 6301, 6302, 6303, 6321, 6322, 6331, 6336, 6337, 6338, 6339, 6340, 6341, 6342, 6343, 6344, 6345, 6346,
        #      6350, 6351, 6352, 6353, 6354, 6355, 6356, 6357, 6358, 6359, 6224, 6225, 6226, 6227, 6229, 6230, 6231, 6232,
        #      6233, 6234, 6235, 6236, 6237, 6239, 6240, 6241, 6242, 6243, 6244, 6245, 6246, 6247, 6248, 6249, 6250, 6251,
        #      6252, 6253, 6254, 6255, 6256, 6257, 6258, 6259, 6260, 6261, 6264, 6265, 6266, 6267, 6268, 6269, 6270, 6271,
        #      6272, 6273, 6274, 6275, 6276, 6277, 6170, 6171, 6172, 6173, 6174, 6175, 6176, 6177, 6178, 6179, 6182, 6183,
        #      6184, 6185, 6186, 6187, 6189, 6190, 6191, 6192, 6193, 6194, 6195, 6196, 6197, 6198, 6199, 6200, 6201, 6202,
        #      6203, 6205, 6206, 6207, 6208, 6209, 6210, 6211, 6212, 6213, 6214, 6215, 6216, 6217, 6218, 6219, 6220, 6221,
        #      6222, 6223, 6101, 6102, 6103, 6104, 6105, 6106, 6107, 6108, 6109, 6110, 6112, 6113, 6115, 6116, 6117, 6118,
        #      6119, 6120, 6121, 6122, 6130, 6131, 6132, 6133, 6134, 6135, 6136, 6137, 6138, 6139, 6140, 6141, 6142, 6143,
        #      6144, 6145, 6146, 6147, 6156, 6157, 6158, 6159, 6160, 6161, 6162, 6163, 6164, 6165, 6166, 6169, 6045, 6046,
        #      6047, 6048, 6049, 6050, 6051, 6052, 6053, 6054, 6055, 6056, 6057, 6058, 6059, 6060, 6061, 6062, 6063, 6065,
        #      6066, 6067, 6068, 6069, 6070, 6071, 6072, 6073, 6074, 6075, 6076, 6077, 6078, 6079, 6080, 6081, 6082, 6083,
        #      6084, 6085, 6086, 6087, 6088, 6089, 6090, 6091, 6092, 6093, 6094, 6100, 2952, 2953, 2954, 2955, 2956, 6000,
        #      6001, 6002, 6003, 6004, 6005, 6006, 6007, 6008, 6009, 6010, 6011, 6012, 6013, 6014, 6015, 6016, 6017, 6018,
        #      6019, 6020, 6021, 6022, 6023, 6024, 6025, 6026, 6027, 6028, 6029, 6030, 6031, 6032, 6033, 6034, 6035, 6036,
        #      6037, 6038, 6039, 6040, 6041, 6042, 6043, 6044, 2825, 2826, 2828, 2829, 2830, 2831, 2832, 2833, 2834, 2835,
        #      2836, 2838, 2839, 2840, 2842, 2843, 2844, 2845, 2846, 2851, 2857, 2858, 2859, 2860, 2861, 2862, 2863, 2864,
        #      2865, 2869, 2871, 2872, 2873, 2874, 2876, 2877, 2878, 2879, 2880, 2881, 2882, 2884, 2885, 2886, 2887, 2888,
        #      2889, 2892, 2950, 2951, 2765, 2767, 2769, 2770, 2771, 2772, 2773, 2774, 2775, 2776, 2777, 2778, 2779, 2780,
        #      2781, 2782, 2783, 2785, 2786, 2787, 2789, 2790, 2791, 2792, 2793, 2794, 2795, 2796, 2797, 2799, 2800, 2801,
        #      2802, 2803, 2804, 2807, 2808, 2809, 2810, 2811, 2812, 2816, 2817, 2818, 2819, 2820, 2821, 2822, 2823, 2824,
        #      2706, 2707, 2708, 2709, 2710, 2712, 2713, 2715, 2718, 2719, 2720, 2721, 2722, 2723, 2724, 2725, 2726, 2727,
        #      2728, 2729, 2731, 2732, 2733, 2734, 2736, 2737, 2741, 2742, 2743, 2744, 2745, 2746, 2747, 2748, 2749, 2750,
        #      2751, 2752, 2753, 2754, 2755, 2756, 2757, 2758, 2759, 2760, 2761, 2762, 2763, 2764, 2617, 2630, 2632, 2633,
        #      2634, 2635, 2636, 2637, 2639, 2648, 2650, 2651, 2652, 2653, 2654, 2655, 2656, 2659, 2660, 2661, 2663, 2664,
        #      2665, 2666, 2667, 2668, 2669, 2670, 2671, 2672, 2673, 2674, 2676, 2677, 2678, 2679, 2680, 2681, 2682, 2683,
        #      2684, 2685, 2686, 2687, 2688, 2689, 2690, 2691, 2702, 2705, 2567, 2568, 2569, 2570, 2571, 2572, 2573, 2574,
        #      2575, 2576, 2577, 2578, 2579, 2580, 2581, 2582, 2583, 2584, 2585, 2586, 2587, 2588, 2589, 2590, 2591, 2592,
        #      2593, 2594, 2595, 2596, 2597, 2598, 2599, 2600, 2601, 2602, 2603, 2604, 2605, 2606, 2607, 2608, 2609, 2610,
        #      2611, 2612, 2613, 2614, 2615, 2616, 2513, 2514, 2515, 2516, 2520, 2521, 2522, 2523, 2524, 2525, 2526, 2527,
        #      2528, 2529, 2530, 2531, 2532, 2533, 2534, 2535, 2536, 2537, 2538, 2539, 2540, 2541, 2542, 2543, 2544, 2545,
        #      2546, 2547, 2548, 2549, 2550, 2551, 2552, 2553, 2554, 2555, 2556, 2557, 2558, 2559, 2561, 2562, 2563, 2564,
        #      2565, 2566, 2463, 2464, 2465, 2466, 2467, 2468, 2469, 2470, 2471, 2472, 2473, 2474, 2475, 2476, 2477, 2478,
        #      2479, 2480, 2481, 2482, 2483, 2484, 2485, 2486, 2487, 2488, 2489, 2490, 2491, 2492, 2493, 2494, 2495, 2496,
        #      2497, 2498, 2499, 2500, 2501, 2502, 2503, 2504, 2505, 2506, 2507, 2508, 2509, 2510, 2511, 2512, 2401, 2409,
        #      2413, 2414, 2417, 2418, 2419, 2420, 2421, 2422, 2423, 2424, 2425, 2426, 2427, 2428, 2429, 2430, 2431, 2432,
        #      2433, 2434, 2435, 2436, 2437, 2438, 2439, 2440, 2441, 2442, 2443, 2444, 2445, 2446, 2447, 2448, 2449, 2450,
        #      2451, 2452, 2453, 2454, 2455, 2456, 2457, 2458, 2459, 2460, 2461, 2462, 2347, 2348, 2349, 2350, 2351, 2352,
        #      2353, 2354, 2355, 2356, 2357, 2358, 2359, 2360, 2361, 2362, 2363, 2364, 2365, 2366, 2367, 2368, 2369, 2370,
        #      2371, 2372, 2373, 2374, 2375, 2377, 2378, 2379, 2380, 2381, 2382, 2383, 2384, 2385, 2386, 2387, 2389, 2390,
        #      2391, 2392, 2393, 2395, 2396, 2397, 2398, 2399, 2286, 2288, 2289, 2290, 2291, 2292, 2293, 2302, 2303, 2304,
        #      2305, 2306, 2307, 2308, 2311, 2312, 2313, 2314, 2315, 2316, 2317, 2318, 2319, 2320, 2321, 2322, 2323, 2324,
        #      2325, 2326, 2327, 2328, 2329, 2330, 2331, 2332, 2333, 2334, 2335, 2336, 2337, 2338, 2339, 2340, 2341, 2342,
        #      2343, 2344, 2345, 2346, 2229, 2230, 2231, 2232, 2233, 2234, 2235, 2236, 2238, 2239, 2240, 2241, 2242, 2244,
        #      2245, 2246, 2247, 2248, 2249, 2250, 2251, 2252, 2253, 2254, 2255, 2256, 2257, 2258, 2259, 2261, 2262, 2263,
        #      2264, 2265, 2266, 2267, 2268, 2269, 2270, 2271, 2272, 2273, 2274, 2275, 2276, 2277, 2278, 2279, 2280, 2281,
        #      2178, 2179, 2180, 2181, 2182, 2183, 2184, 2185, 2186, 2187, 2188, 2189, 2190, 2191, 2192, 2193, 2194, 2195,
        #      2196, 2197, 2198, 2199, 2200, 2201, 2202, 2203, 2205, 2206, 2207, 2208, 2209, 2210, 2211, 2212, 2213, 2214,
        #      2215, 2216, 2217, 2218, 2219, 2220, 2221, 2222, 2223, 2224, 2225, 2226, 2227, 2228, 2124, 2125, 2126, 2127,
        #      2128, 2129, 2130, 2131, 2132, 2133, 2134, 2135, 2136, 2137, 2138, 2139, 2141, 2142, 2143, 2144, 2145, 2146,
        #      2147, 2148, 2149, 2150, 2151, 2152, 2153, 2154, 2155, 2156, 2157, 2158, 2159, 2160, 2161, 2162, 2163, 2164,
        #      2165, 2166, 2167, 2168, 2169, 2170, 2171, 2172, 2173, 2174, 2073, 2074, 2075, 2076, 2077, 2078, 2079, 2080,
        #      2081, 2082, 2083, 2084, 2085, 2086, 2087, 2088, 2090, 2091, 2092, 2093, 2094, 2095, 2096, 2097, 2098, 2099,
        #      2100, 2101, 2102, 2103, 2104, 2105, 2106, 2107, 2108, 2109, 2110, 2111, 2112, 2113, 2114, 2115, 2116, 2117,
        #      2118, 2119, 2120, 2121, 2122, 2123, 2022, 2023, 2024, 2025, 2026, 2027, 2028, 2030, 2031, 2032, 2033, 2034,
        #      2035, 2036, 2037, 2038, 2039, 2040, 2041, 2042, 2043, 2044, 2045, 2046, 2047, 2048, 2049, 2050, 2051, 2052,
        #      2053, 2054, 2055, 2056, 2057, 2058, 2059, 2060, 2061, 2062, 2063, 2064, 2065, 2066, 2067, 2068, 2069, 2070,
        #      2071, 2072, 543, 544, 545, 546, 547, 548, 549, 550, 551, 552, 553, 554, 555, 556, 557, 558, 559, 560, 561,
        #      562, 563, 564, 565, 566, 569, 570, 571, 572, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009,
        #      2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 146, 147, 149, 150, 151, 153, 154,
        #      500, 501, 502, 503, 504, 505, 506, 507, 508, 509, 510, 511, 512, 513, 514, 515, 516, 517, 518, 519, 520,
        #      521, 522, 523, 524, 525, 526, 527, 528, 529, 530, 531, 532, 533, 534, 535, 536, 537, 538, 539, 540, 541,
        #      542, 1, 2, 3, 4, 5, 6, 7, 9, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114,
        #      115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 127, 129, 130, 131, 132, 133, 135, 136, 137, 138,
        #      139, 140, 141, 143, 144, 145]
        a=[10226, 10233, 10236, 10195, 10204, 10207, 10210, 10124, 10125, 10126, 10139, 10140, 10142, 10146, 10073, 10079, 10080, 10089, 10107, 10113, 10118, 10025, 10026, 10032, 10033, 10039, 10040, 10044, 10055, 10071, 6405, 6406, 6407, 6408, 6409, 6410, 6279, 6280, 6281, 6284, 6285, 6286, 6287, 6288, 6289, 6290, 6291, 6292, 6293, 6294, 6295, 6296, 6297, 6298, 6299, 6300, 6301, 6302, 6303, 6321, 6322, 6331, 6336, 6337, 6338, 6339, 6340, 6341, 6342, 6343, 6344, 6345, 6346, 6350, 6351, 6352, 6353, 6354, 6355, 6356, 6357, 6358, 6359, 6224, 6225, 6226, 6227, 6229, 6230, 6231, 6232, 6233, 6234, 6235, 6236, 6237, 6239, 6240, 6241, 6242, 6243, 6244, 6245, 6246, 6247, 6248, 6249, 6250, 6251, 6252, 6253, 6254, 6255, 6256, 6257, 6258, 6259, 6260, 6261, 6264, 6265, 6266, 6267, 6268, 6269, 6270, 6271, 6272, 6273, 6274, 6275, 6276, 6277, 6170, 6171, 6172, 6173, 6174, 6175, 6176, 6177, 6178, 6179, 6182, 6183, 6184, 6185, 6186, 6187, 6189, 6190, 6191, 6192, 6193, 6194, 6195, 6196, 6197, 6198, 6199, 6200, 6201, 6202, 6203, 6205, 6206, 6207, 6208, 6209, 6210, 6211, 6212, 6213, 6214, 6215, 6216, 6217, 6218, 6219, 6220, 6221, 6222, 6223, 6101, 6102, 6103, 6104, 6105, 6106, 6107, 6108, 6109, 6110, 6112, 6113, 6115, 6116, 6117, 6118, 6119, 6120, 6121, 6122, 6130, 6131, 6132, 6133, 6134, 6135, 6136, 6137, 6138, 6139, 6140, 6141, 6142, 6143, 6144, 6145, 6146, 6147, 6156, 6157, 6158, 6159, 6160, 6161, 6162, 6163, 6164, 6165, 6166, 6169, 6045, 6046, 6047, 6048, 6049, 6050, 6051, 6052, 6053, 6054, 6055, 6056, 6057, 6058, 6059, 6060, 6061, 6062, 6063, 6065, 6066, 6067, 6068, 6069, 6070, 6071, 6072, 6073, 6074, 6075, 6076, 6077, 6078, 6079, 6080, 6081, 6082, 6083, 6084, 6085, 6086, 6087, 6088, 6089, 6090, 6091, 6092, 6093, 6094, 6100, 2952, 2953, 2954, 2955, 2956, 6000, 6001, 6002, 6003, 6004, 6005, 6006, 6007, 6008, 6009, 6010, 6011, 6012, 6013, 6014, 6015, 6016, 6017, 6018, 6019, 6020, 6021, 6022, 6023, 6024, 6025, 6026, 6027, 6028, 6029, 6030, 6031, 6032, 6033, 6034, 6035, 6036, 6037, 6038, 6039, 6040, 6041, 6042, 6043, 6044, 2825, 2826, 2828, 2829, 2830, 2831, 2832, 2833, 2834, 2835, 2836, 2838, 2839, 2840, 2842, 2843, 2844, 2845, 2846, 2851, 2857, 2858, 2859, 2860, 2861, 2862, 2863, 2864, 2865, 2869, 2871, 2872, 2873, 2874, 2876, 2877, 2878, 2879, 2880, 2881, 2882, 2884, 2885, 2886, 2887, 2888, 2889, 2892, 2950, 2951, 2765, 2767, 2769, 2770, 2771, 2772, 2773, 2774, 2775, 2776, 2777, 2778, 2779, 2780, 2781, 2782, 2783, 2785, 2786, 2787, 2789, 2790, 2791, 2792, 2793, 2794, 2795, 2796, 2797, 2799, 2800, 2801, 2802, 2803, 2804, 2807, 2808, 2809, 2810, 2811, 2812, 2816, 2817, 2818, 2819, 2820, 2821, 2822, 2823, 2824, 2706, 2707, 2708, 2709, 2710, 2712, 2713, 2715, 2718, 2719, 2720, 2721, 2722, 2723, 2724, 2725, 2726, 2727, 2728, 2729, 2731, 2732, 2733, 2734, 2736, 2737, 2741, 2742, 2743, 2744, 2745, 2746, 2747, 2748, 2749, 2750, 2751, 2752, 2753, 2754, 2755, 2756, 2757, 2758, 2759, 2760, 2761, 2762, 2763, 2764, 2617, 2630, 2632, 2633, 2634, 2635, 2636, 2637, 2639, 2648, 2650, 2651, 2652, 2653, 2654, 2655, 2656, 2659, 2660, 2661, 2663, 2664, 2665, 2666, 2667, 2668, 2669, 2670, 2671, 2672, 2673, 2674, 2676, 2677, 2678, 2679, 2680, 2681, 2682, 2683, 2684, 2685, 2686, 2687, 2688, 2689, 2690, 2691, 2702, 2705, 2567, 2568, 2569, 2570, 2571, 2572, 2573, 2574, 2575, 2576, 2577, 2578, 2579, 2580, 2581, 2582, 2583, 2584, 2585, 2586, 2587, 2588, 2589, 2590, 2591, 2592, 2593, 2594, 2595, 2596, 2597, 2598, 2599, 2600, 2601, 2602, 2603, 2604, 2605, 2606, 2607, 2608, 2609, 2610, 2611, 2612, 2613, 2614, 2615, 2616, 2513, 2514, 2515, 2516, 2520, 2521, 2522, 2523, 2524, 2525, 2526, 2527, 2528, 2529, 2530, 2531, 2532, 2533, 2534, 2535, 2536, 2537, 2538, 2539, 2540, 2541, 2542, 2543, 2544, 2545, 2546, 2547, 2548, 2549, 2550, 2551, 2552, 2553, 2554, 2555, 2556, 2557, 2558, 2559, 2561, 2562, 2563, 2564, 2565, 2566, 2463, 2464, 2465, 2466, 2467, 2468, 2469, 2470, 2471, 2472, 2473, 2474, 2475, 2476, 2477, 2478, 2479, 2480, 2481, 2482, 2483, 2484, 2485, 2486, 2487, 2488, 2489, 2490, 2491, 2492, 2493, 2494, 2495, 2496, 2497, 2498, 2499, 2500, 2501, 2502, 2503, 2504, 2505, 2506, 2507, 2508, 2509, 2510, 2511, 2512, 2401, 2409, 2413, 2414, 2417, 2418, 2419, 2420, 2421, 2422, 2423, 2424, 2425, 2426, 2427, 2428, 2429, 2430, 2431, 2432, 2433, 2434, 2435, 2436, 2437, 2438, 2439, 2440, 2441, 2442, 2443, 2444, 2445, 2446, 2447, 2448, 2449, 2450, 2451, 2452, 2453, 2454, 2455, 2456, 2457, 2458, 2459, 2460, 2461, 2462, 2347, 2348, 2349, 2350, 2351, 2352, 2353, 2354, 2355, 2356, 2357, 2358, 2359, 2360, 2361, 2362, 2363, 2364, 2365, 2366, 2367, 2368, 2369, 2370, 2371, 2372, 2373, 2374, 2375, 2377, 2378, 2379, 2380, 2381, 2382, 2383, 2384, 2385, 2386, 2387, 2389, 2390, 2391, 2392, 2393, 2395, 2396, 2397, 2398, 2399, 2286, 2288, 2289, 2290, 2291, 2292, 2293, 2302, 2303, 2304, 2305, 2306, 2307, 2308, 2311, 2312, 2313, 2314, 2315, 2316, 2317, 2318, 2319, 2320, 2321, 2322, 2323, 2324, 2325, 2326, 2327, 2328, 2329, 2330, 2331, 2332, 2333, 2334, 2335, 2336, 2337, 2338, 2339, 2340, 2341, 2342, 2343, 2344, 2345, 2346, 2229, 2230, 2231, 2232, 2233, 2234, 2235, 2236, 2238, 2239, 2240, 2241, 2242, 2244, 2245, 2246, 2247, 2248, 2249, 2250, 2251, 2252, 2253, 2254, 2255, 2256, 2257, 2258, 2259, 2261, 2262, 2263, 2264, 2265, 2266, 2267, 2268, 2269, 2270, 2271, 2272, 2273, 2274, 2275, 2276, 2277, 2278, 2279, 2280, 2281, 2178, 2179, 2180, 2181, 2182, 2183, 2184, 2185, 2186, 2187, 2188, 2189, 2190, 2191, 2192, 2193, 2194, 2195, 2196, 2197, 2198, 2199, 2200, 2201, 2202, 2203, 2205, 2206, 2207, 2208, 2209, 2210, 2211, 2212, 2213, 2214, 2215, 2216, 2217, 2218, 2219, 2220, 2221, 2222, 2223, 2224, 2225, 2226, 2227, 2228, 2124, 2125, 2126, 2127, 2128, 2129, 2130, 2131, 2132, 2133, 2134, 2135, 2136, 2137, 2138, 2139, 2141, 2142, 2143, 2144, 2145, 2146, 2147, 2148, 2149, 2150, 2151, 2152, 2153, 2154, 2155, 2156, 2157, 2158, 2159, 2160, 2161, 2162, 2163, 2164, 2165, 2166, 2167, 2168, 2169, 2170, 2171, 2172, 2173, 2174, 2073, 2074, 2075, 2076, 2077, 2078, 2079, 2080, 2081, 2082, 2083, 2084, 2085, 2086, 2087, 2088, 2090, 2091, 2092, 2093, 2094, 2095, 2096, 2097, 2098, 2099, 2100, 2101, 2102, 2103, 2104, 2105, 2106, 2107, 2108, 2109, 2110, 2111, 2112, 2113, 2114, 2115, 2116, 2117, 2118, 2119, 2120, 2121, 2122, 2123, 2022, 2023, 2024, 2025, 2026, 2027, 2028, 2030, 2031, 2032, 2033, 2034, 2035, 2036, 2037, 2038, 2039, 2040, 2041, 2042, 2043, 2044, 2045, 2046, 2047, 2048, 2049, 2050, 2051, 2052, 2053, 2054, 2055, 2056, 2057, 2058, 2059, 2060, 2061, 2062, 2063, 2064, 2065, 2066, 2067, 2068, 2069, 2070, 2071, 2072, 543, 544, 545, 546, 547, 548, 549, 550, 551, 552, 553, 554, 555, 556, 557, 558, 559, 560, 561, 562, 563, 564, 565, 566, 570, 571, 150, 151, 153, 154, 502, 504, 507, 508, 510, 511, 522, 523, 530, 7, 9]
        for i in a:
            r = Request('https://loj.ac/problem/%d/testdata/download' % i, callback=self.parse_post)
            r.meta["num"] = i
            yield r

    def parse_post(self, response):
        i = response.meta["num"]

        filename = '/Users/mac/Desktop/rename/package/problem%d.zip' % i
        r = requests.get('https://loj.ac/problem/%d/testdata/download' % i)
        with open(filename, "wb") as f:
            f.write(r.content)
        yield
