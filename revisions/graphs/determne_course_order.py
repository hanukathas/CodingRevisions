def determne_course_order(tables: list):
    result = []
    processed = set()

    def get_dependecies(course) -> list:
        pass
    def process(table):
        if table in processed:
            return
        dependencies = get_dependecies(table)

        for dep in dependencies:
            if dep not in processed:
                process(dep)

        if table not in processed:
            processed.add(table)
            result.append(table)


    for table in tables:
        process(table)