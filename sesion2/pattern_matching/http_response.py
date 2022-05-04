def http_response(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 200:
            return "Response OK"
        case _:
            return "Something's wrong with the Internet"
            
           
print(http_response("404"))
print(http_response("400"))
print(http_response("500"))
print(http_response("200"))
