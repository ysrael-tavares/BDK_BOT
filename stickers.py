def sticker(number):
    switcher={
        1: "CAACAgQAAxkBAAP0X-_CRJamQ3KAUbABQHIUTzGuAu4AAggJAAIYMKoFpVQX119ZdBgeBA",
        4: "CAACAgQAAxkBAAIBgV_v1brqn0lhcErgMwYrE8A--zqGAAIxBQACGDCqBTRtlxGjctxhHgQ",
        6: "CAACAgQAAxkBAAIBgF_v1Zm-KaiWMvfVeFN6JYAoDhTwAAKJBQACGDCqBUKwBrWUm6RyHgQ",
        8: "CAACAgQAAxkBAAIBf1_v1W2c41hYJsw8i7VZTSP0aw3CAAJMCgACGDCqBTwTpgz3aXy1HgQ",
        10:"CAACAgQAAxkBAAIBeV_v1OWfHVE_4jj5Xi3FBw6mZe1fAALGAgACGDCqBfS3X20j0QmEHgQ",
        12:"CAACAgQAAxkBAAIBeF_v1LSxREbG8-_w3rVrYgAB6xKZpwACRgoAAhgwqgULwgyy8bO7gB4E",
        20:"CAACAgIAAxkBAAPuX--_xSb3kFFpDw2q0Ank0xHHMCYAAmgBAAIQGm0i9TccKfYXpG8eBA"
    }

    return switcher.get(number,"Erro")
