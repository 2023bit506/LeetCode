def compress(chars):
        result = []
        ct = ""
        for i in chars:
            if i in result:
                continue
            else:
                result.append(i)
                if chars.count(i) == 1:
                    continue
                else:
                    ct += (str(chars.count(i)))
                    
        result.extend(ct)
            
        return result
        # return ct
    
print(compress(["a","a","b","b","c","c","c"]))
print(compress(["a"]))
print(compress(["a","b","b","b","b","b","b","b","b","b","b","b","b"]))