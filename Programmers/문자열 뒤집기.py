def solution(my_string):
    reverse_str = "".join(reversed(my_string))
    return reverse_str # my_string[::-1]

# reversed("021") => ["1", "2", "0"]
# "".join(["1", "2", "0"]) => "120"
