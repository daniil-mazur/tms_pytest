def my_shiny_new_decorator(function_to_decorate):
    def the_wrapper_around_the_original_function():
        print("Я - код, который отработает до вызова функции")
        function_to_decorate()  # Сама функция
        print("А я - код, срабатывающий после")

    return the_wrapper_around_the_original_function


def stand_alone_function():
    print("Я простая одинокая функция, ты ведь не посмеешь меня изменять?")


stand_alone_function()

stand_alone_function_decorated = my_shiny_new_decorator(stand_alone_function)
stand_alone_function_decorated()


@my_shiny_new_decorator
def stand_alone_function_always_decorated():
    print("Я простая одинокая функция, я уже задекорирована")


stand_alone_function_always_decorated()
