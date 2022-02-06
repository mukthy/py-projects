is_magician = False
is_expert = True
# chek if magician AND expert: "you are a master magician" ID
# check if magician but not expert: "at least you're getting there"
# if you're not a magician: "YOu need magic powers"

if is_magician and is_expert:
    print("you are a master magician")
elif is_magician and not is_expert:
    print("at least you're getting there")
elif not is_magician:
    print("You need magic powers")
