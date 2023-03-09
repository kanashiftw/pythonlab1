def non_empty(funk):
    def wrapper():
        res = funk()
        count = 0
        for i in res:
            if i == '' or i == None:
                res.pop(count)
            count+=1
        return res
    return wrapper

@non_empty
def get_pages():
    return ['shadowfiend', 'wywf?', '',  'lie']

print(get_pages())
