import wolframalpha as wa
client = wa.Client("834JUH-LUV8EVJ928")

queries = {"(x^2 - 4)" : [], "(x^2 - 4)(x - 1)(x+ 4)" : []}

for query in queries.keys():
    query_result = client.query(query)
    for pod in query_result:
        if "alternate form" in pod.title.lower():
            for item in pod:
                queries[query].append(item.text)

for key in queries.keys():
    print key, ": ", queries[key]


