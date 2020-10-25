def get_list(local, user=None):
    u"""Lista para criação do menu.

        menulist = [<nivel do menu>, <label do menu>, <url>, <img css>,
            <flag p/ mostrar menu>]
            <nivel do menu> = 1, 2, 3
            <img css> = icones contidos no font-awesome,
            http://fortawesome.github.io/Font-Awesome/icons/

    """
    menulist = list()

    menulist.append([True, 'Dashboard', '/index/',
                     'dashboard', True])
    menulist.append([True, 'Produtos', '/produtos/',
                     'produtos', True])


    for menu in menulist:
        if local == menu[1]:
            menu[0] = True
        else:
            menu[0] = False
    # print(menulist)

    return menulist
