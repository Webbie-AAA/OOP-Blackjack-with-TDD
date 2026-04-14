# pylint: skip-file
from datetime import datetime, timedelta
from blockbuster_oop import Video, Customer, VideoStore, VendingMachine, DVD, Rental
import pytest


def test_customer_name():
    john = Customer('John', 'Smith', '24/01/1980')
    assert john.get_full_name() == 'John Smith'


def test_video_release_after_current_year():
    with pytest.raises(Exception):
        Video('The Dreyfus Affair', 2027, 13)


def test_video_has_title():
    with pytest.raises(Exception):
        Video('Vampires vs Fairies', 2010, None)


def test_customer_full_name():
    first_customer = Customer("Penelope", "Pig", "13/08/2006")
    assert first_customer.get_full_name() == "Penelope Pig"


def test_customer_name_is_string():
    with pytest.raises(TypeError):
        Customer(None, None, "19/02/1992")


def test_customer_birth_year_after_1900():
    with pytest.raises(ValueError):
        Customer("Abc", "Def", "1800")


def test_customer_birth_year_before_this_year():
    with pytest.raises(ValueError):
        Customer("Abc", "Def", "2200")


def test_customer_get_age_correct_calculation():
    customer = Customer("prince", "Turner", "11/11/2000")
    assert customer.get_age() == 25


def test_customer_DOB_correct_format():
    with pytest.raises(ValueError):
        Customer("Apple", "Batman", "111")


def test_video_store_min_1item():
    with pytest.raises(ValueError):
        VideoStore([])


def test_video_store_max_10items():
    with pytest.raises(ValueError):
        VideoStore([Video(f"Movie {i}", 2000, 100) for i in range(11)])


def test_is_available_returns_true_when_available():
    v1 = Video("TNT", 1999, 170)
    store = VideoStore([v1])
    assert store.is_available(v1) is True


def test_rent_video_successfully():
    v2 = Video("Maze Runner", 2012, 300)
    store = VideoStore([v2])
    john = Customer("John", "Doe", "01/01/1990")
    result = store.rent_video("Maze Runner", john)
    assert isinstance(result, Rental)
    assert store.availability["Maze Runner"] is False


def test_video_rewind_logic():
    vhs = Video("ABC", 1965, 116)
    vhs.watch()
    with pytest.raises(Exception):
        vhs.watch()


def test_video_rewind_and_watch_again():
    vhs = Video("ABC", 1965, 116)
    vhs.watch()
    vhs.rewind()
    vhs.watch()


def test_video_price_extra_long_runtime_and_current_year():
    current_year = datetime.now().year
    video = Video("ABD", current_year, 245)
    price = video.rental_price()
    assert price == 2000


def test_video_price_old_and_short():
    old_video = Video("Tweety", 1955, 81)
    assert old_video.rental_price() == 500


def test_dvd_price_new_and_extra_long():
    current_year = datetime.now().year
    new_dvd = DVD("X-MEN", current_year, 330)
    assert new_dvd.rental_price() == 1200


def test_dvd_price_old_and_short():
    old_dvd = DVD("Dracula", 1945, 94)
    assert old_dvd.rental_price() == 1200


# I'm aware that I haven't converted fines to Pence. I'll do that later.

def test_fine_accrued_on_late_return():
    john = Customer("John", "Doe", "01/01/1990")
    vid = Video("The Matrix", 1999, 136)
    store = VideoStore([vid])

    due_date = datetime.now() - timedelta(days=5)
    rental = Rental(john, vid, due_date)

    today_str = datetime.now().strftime("%d/%m/%Y")
    store.return_video(rental, today_str)

    assert john.outstanding_fine == 10


def test_rent_blocked_by_high_fine():
    bad_customer = Customer("Bob", "Max", "01/08/1999")
    bad_customer.outstanding_fine = 55

    vid = Video("The Matrix", 1999, 136)
    store = VideoStore([vid])

    with pytest.raises(Exception):
        store.rent_video("The Matrix", bad_customer)


def test_pay_fine_restore_balance():
    bad_customer = Customer("Bob", "Max", "01/08/1999")
    bad_customer.outstanding_fine = 55

    bad_customer.pay_off_fine()

    assert bad_customer.outstanding_fine == 0


def new_release_and_late_fine():
    current_year = datetime.now().year
    new_dvd = DVD("X-MEN", current_year, 330)
    bad_customer = Customer("Bob", "Max", "01/08/1999")

    rental = Rental(bad_customer, new_dvd, datetime.now() - timedelta(days=1))

    store = VideoStore([new_dvd])
    store.return_video(rental, datetime.now().strftime('%d/%m/%Y'))

    assert bad_customer.outstanding_fine == 15


def test_vending_machine_too_many_videos():
    many_videos = [Video(f"Movie {i}", 2000, 100) for i in range(6)]

    with pytest.raises(ValueError):
        VendingMachine(many_videos)


def test_find_video_not_in_store():
    v1 = Video("The Matrix", 1999, 136)
    store = VideoStore([v1])

    with pytest.raises(ValueError):
        store.find_video_by_title("Shrek")


def test_cannot_rent_already_rented_video():
    v1 = Video("abc", 1986, 110)
    store = VideoStore([v1])
    john = Customer("John", "Smith", "01/01/1980")
    jane = Customer("Jane", "Doe", "01/01/1990")

    store.rent_video("abc", john)

    with pytest.raises(Exception):
        store.rent_video("abc", jane)


def test_cannot_add_movie_from_future():
    future_year = datetime.now().year + 1

    with pytest.raises(Exception):
        Video("XYZ", future_year, 120)
