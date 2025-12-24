def sort_on(items):
    return items["num"]

def get_num_words(file_contents) -> int:
    counts = file_contents.split()
    total_count = len(counts)
    return total_count

def get_num_letter(file_contents) -> set:
    words = list(file_contents)
    d = {}
    for word in words:
        if word not in d:
            d[word] = 1
        else:
            d[word] += 1

    return d

def sort_dict(d):
    results = []

    for key,value in d.items():
        results.append({"char": key, "num": value})

    results.sort(reverse=True,key=sort_on)
    
    return results
