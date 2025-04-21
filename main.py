from ui import *
from service import *
from filles_for_complexity import *

if __name__ == '__main__':
    service = MasinaService()
    # service.test_search()
    # service.test_sort()
    meniu = UserCommandLineInterface(service)
    meniu.run()
    main()