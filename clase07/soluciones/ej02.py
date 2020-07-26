def eval_loop():
    prompt = "> "
    last = None
    while True:
        line = input(prompt)
        if line == "exit":
            return last
            break
        last = eval(line)
        print(last)

print("Last: " + str(eval_loop()))
