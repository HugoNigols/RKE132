

def clean_my_list(some_list):

    '''
        Puhastab antud nimekirja elementide algusest ja lõpust tühikud ja reavahed.
        Args:
            some_list (list): Nimekiri, mis sisaldab puhastamata tekstielemente (nt faili read koos \n märgiga).

        Returns:
            list: Uus nimekiri, kus kõik elemendid on puhastatud liigsetest tühikutest ja reavahetustest.
    '''


    clean_list = []

    for element in some_list:
        clean_element = element.strip()
        clean_list.append(clean_element)

    return clean_list
