"""CP1404 Test using Wikipedia API for python."""
import wikipedia
import warnings


def search_wiki():
    """
    Search Wikipedia for user input string.
    Note: Quotation wrapper needed for the API call to avoid html parser error when returning summary information
    """
    warnings.filterwarnings("ignore")  # disambiguations options triggers a user warning about parsing html
    search_string = "\'" + input("Enter Wikipedia search: ") + "\'"
    while search_string != "\'\'":
        try:
            wiki_page = wikipedia.page(search_string)
            print("{}\n{}\n{}".format(wiki_page.title, wiki_page.url, wiki_page.summary))
        except wikipedia.exceptions.DisambiguationError as e:
            # print(e.options)
            option_count = 0
            options_list = []
            for n in range(0, len(e.options)):
                if e.options[n][0:9] != "All pages":  # only want options leading to specific pages
                    print("{}. {}".format(n + 1, e.options[n]))
                    option_count += 1
                    options_list.append(e.options[n])
            search_option = input("Enter Wiki disambiguation number: ")
            while search_option != "":
                try:
                    if int(search_option) in range(1, option_count + 1):
                        try:
                            wiki_page = wikipedia.page(options_list[int(search_option) - 1])
                            print("{}\n{}\n{}".format(wiki_page.title, wiki_page.url, wiki_page.summary))
                        except:
                            print("Selection does not return a page. Choose another.")
                    else:
                        print("Invalid selection")
                except:
                    print("Invalid selection (input must be integer)")
                search_option = input("Enter Wiki disambiguation number: ")
        search_string = "\'" + input("Enter Wikipedia search: ") + "\'"

search_wiki()

