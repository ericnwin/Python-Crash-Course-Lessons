

favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'gaby': ['javascript'],
    'alex': ['c', 'python'],
}

for names, languages in favorite_languages.items():
    if len(languages) == 1:
        print(f"{names.title()}'s favorite language is:'")
        for language in languages:
            print(f"\t{language.title()}")
    else:
        print(f"{names.title()}'s favorite languages are:")
        for language in languages:
            print(f"\t{language.title()}")
