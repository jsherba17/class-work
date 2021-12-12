text = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque dictum, ipsum ut feugiat elementum, ex magna rhoncus enim, quis tincidunt turpis augue nec leo. Quisque maximus finibus rutrum. Integer non urna sit amet odio faucibus mattis. Morbi auctor lacus arcu, ac suscipit diam placerat ac. Nulla aliquam mi vel vestibulum bibendum. Mauris et erat felis. Nam aliquam, nibh sed dapibus accumsan, neque justo venenatis metus, et luctus magna enim at turpis. Donec sollicitudin elit magna, eu dapibus elit laoreet eu. Maecenas at sodales quam. Duis tristique ornare metus sit amet molestie. Cras malesuada justo ut rutrum volutpat. Nullam quis risus eu nisi dignissim feugiat at et justo. Fusce vitae odio sed est fermentum aliquam eget at ligula. Sed eu efficitur dui. Ut id lacinia ipsum. Pellentesque posuere turpis pharetra, maximus dui sed, efficitur sem. """
my_file = open('lorem.txt', 'w')
my_file.write(text)
my_file.close()

if 'w' not in text:
    print("Да, в тексте есть w")
else:
    print("Нет, в тексте нет w")
