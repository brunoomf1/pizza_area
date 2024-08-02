def translateListToJson(item):
    response = {}
    for i in item:
        obj = {}
        obj['uf_id'] = i[0]
        obj['uf_name'] = i[1]
        response[i[2]] = obj
    return response
