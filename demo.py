"""
批量导入数据库
"""

def input_data():
    import json
    jstr = "oj.json"
    with open(jstr, "r") as f:
        a = json.load(f)
    # 1.创建父分类一本通
    parent_tag = ProblemTag.objects.filter(name="一本通")
    user = User.objects.get(username="jamie")
    if not parent_tag:
        parent_tag = ProblemTag.objects.create(name="一本通")
    else:
        parent_tag = parent_tag[0]

    for e, i in enumerate(a):
        # 2.创建问题子分类
        tag = i["category"]
        tags = []

        # 3.处理问题标签
        for j in tag.split(" ,"):
            # 为空判断
            if j:
                t = ProblemTag.objects.filter(name=j)
                if not t:
                    t = ProblemTag.objects.create(name=j, parent=parent_tag)
                else:
                    t = t[0]
                tags.append(t)

        # 4.创建问题
        p = Problem.objects.create(
            _id=str(900 + e),
            title="[一本通%s]%s" % (i["number"], i["title"]),
            description=desc_is_null(i["desc"]),
            input_description=desc_is_null(i["input_desc"]),
            output_description=desc_is_null(i["output_desc"]),
            samples=[{"input": i["example_input"], "output": i["example_output"]}],
            hint=desc_is_null(i["tig"]),
            rule_type="OI",
            difficulty="Low",
            memory_limit=256,
            time_limit=1000,
            languages=list(["Java", "Python2", "C++", "C", "Python3"]),
            source="一本通",
            test_case_score=dict(),
            template=dict(),
            created_by=user,
            test_case_id=""
        )
        p.tags.set(tags)
    return "ok"


def desc_is_null(data):
    if data:
        return "<p>%s</p>" % data
    else:
        return " "
