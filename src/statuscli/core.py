def summarize(items):
    result={}
    for item in items:
        s=str(item.get("status","unknown")).lower();result[s]=result.get(s,0)+1
    return dict(sorted(result.items()))
