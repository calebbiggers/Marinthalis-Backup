from xmlrpc.client import ServerProxy


def main():
    s = ServerProxy('https://dnd5e.www.wikidot.com/xml-rpc-api.php')
    s.system.listMethods()


if __name__ == '__main__':
    main()
