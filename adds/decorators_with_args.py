def a_decorator_passing_arbitrary_arguments(function_to_decorate):
    def a_wrapper_accepting_arbitrary_arguments(*args, **kwargs):
        print("Передали ли мне что-нибудь?:")
        print("Args: ", args)
        print("Kwargs:", kwargs)
        function_to_decorate(*args, **kwargs)
    return a_wrapper_accepting_arbitrary_arguments

# @a_decorator_passing_arbitrary_arguments
# def function_with_no_argument():
#     print("Python is cool, no argument here.")
#
# function_with_no_argument()
# @a_decorator_passing_arbitrary_arguments
# def function_with_arguments(a, b, c):
#     print(a, b, c)
#
# function_with_arguments(1, 2, 3)
# @a_decorator_passing_arbitrary_arguments
# def function_with_named_arguments(a, b, c, platypus):
#     print("Любят ли {}, {} и {} утконосов? {}".format(a, b, c, platypus))
#
# function_with_named_arguments("Билл", "Линус", "Стив", platypus="Определенно!")
# class Mary(object):
#     def __init__(self):
#         self.age = 31
#     @a_decorator_passing_arbitrary_arguments
#     def sayYourAge(self, lie=3): # Теперь мы можем указать значение по умолчанию
#         print("Мне {} лет, а ты бы сколько дал?".format(self.age + lie))
#
# m = Mary()
# m.sayYourAge()
