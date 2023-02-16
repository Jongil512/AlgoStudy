def activa_W(keyword, history, answer):
    for sent in history:
        for word in sent.split(" "):
            if keyword == word:
                answer.append(sent)


def active_WC(keyword, history, answer):
    if keyword[-1] == "*":
        for sent in history:
            for word in sent.split(" "):
                if keyword[:-1] in word:
                    answer.append(sent)
                    break
    elif keyword.count("*") >= 2:
        activa_W(keyword, answer)


def search(options, keyword, history):
    answer = []
    activate = {
        "W": False,
        "R": False,
        "WC": False
    }

    for option in options:
        activate[option[0]] = True

    if activate["W"]:
        activa_W(keyword, history, answer)

    elif activate["WC"]:
        if keyword == "*":
            answer = history
        else:
            active_WC(keyword, history, answer)


    if activate["R"]:
        for i in range(len(answer)):
            if len(answer[i]) >= 10:
                answer[i] = answer[i][:10] + '...'

    if len(answer) == 0:
        answer = ["empty"]

    return answer

T = 1
for tc in range(1, T+1):
    options = [
        ["W", "T"],
        # ["WC", "T"],
        ["R", "T"]
    ]
    keyword = "he"
    history = ["hello i'm jongil",
               "hi i'm jongil",
               "hello there",
               "he is handsome",
               "he* zzzkjebkjsv"]
    print(search(options, keyword, history))