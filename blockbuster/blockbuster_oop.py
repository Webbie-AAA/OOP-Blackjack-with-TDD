""""This module is a 90s rental system for a BlockBuster video"""
from datetime import datetime, timedelta


class Video:
    """Represents a physical video tape (VHS) available for rent."""

    def __init__(self, title: str, year: int, runtime: int):
        self.title = title
        self.year = year
        self.runtime = runtime
        self.is_rewound = True

        current_year = datetime.now().year

        if int(self.year) < 1900:
            raise Exception("Invalid date. Please enter year after 1990")

        if int(self.year) > current_year:
            raise Exception("Invalid date. This year doesn't exist yet!")

        if not isinstance(self.runtime, int):
            raise ValueError("Please enter an integer value")

        if not isinstance(self.title, str):
            raise ValueError("Please enter a string value")

    def display_title(self):
        """Returns a formatted string of the title and year."""
        return f"{self.title.title()} ({self.year})"

    def rental_price(self):
        """Calculates rental price based on year and runtime"""
        current_year = datetime.now().year
        total_price_pence = 0
        if self.year == current_year:
            total_price_pence += 1000
        else:
            total_price_pence += 500
        if self.runtime > 240:
            total_price_pence *= 2
        return total_price_pence

    def display_price(self):
        """Returns the rental price formatted as a GBP string (e.g., £5.00)."""
        return f"£{(self.rental_price())/100:.2f}"

    def watch(self):
        """Simulates watching the video."""
        if self.is_rewound is True:
            self.is_rewound = False
        else:
            raise Exception(
                "This video needs to be rewound (it has already been watched")

    def rewind(self):
        if self.is_rewound is False:
            self.is_rewound = True
        else:
            raise Exception("This video has already been rewound.")


class Customer:
    """Represents a store member who can rent videos."""

    def __init__(self, first_name: str, last_name: str, date_of_birth: datetime):
        """Initializes a customer profile."""
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.outstanding_fine = 0

        if not isinstance(self.first_name, str) or not isinstance(self.last_name, str):
            raise TypeError("Names must be strings")

        format_str = '%d/%m/%Y'
        try:
            dob = datetime.strptime(self.date_of_birth, format_str)
        except ValueError:
            raise ValueError(
                f"{self.date_of_birth} is not in DD/MM/YYYY format")

        if dob.year < 1900 or dob.year > dob.now().year:
            raise ValueError(
                "Birth year must be greater than 1900 and before the current year")

    def get_full_name(self):
        """Returns the customer's title-cased full name."""
        return f"{self.first_name.title()} {self.last_name.title()}"

    def get_age(self):
        """Calculates current age based on DOB."""
        format_str = '%d/%m/%Y'
        year_of_birth = (datetime.strptime(
            self.date_of_birth, format_str)).year
        current_year = datetime.now().year
        age = current_year - year_of_birth
        return age

    # Treating date_of_birth as string when it's datetime object
    def pay_off_fine(self):
        """Resets the customer's outstanding fine to zero."""
        self.outstanding_fine = 0


class Rental:
    """A record of a specific rental transaction."""

    def __init__(self, renting_customer: Customer, rented_video: Video, due_date: datetime):
        """Links a customer to a video with a return deadline."""
        if not isinstance(renting_customer, Customer):
            raise ValueError("The customer is not our customer")
        if not isinstance(rented_video, Video):
            raise ValueError("The video is not from our collection")
        if not isinstance(due_date, datetime):
            raise ValueError("Please enter a datetime object")

        self.renting_customer = renting_customer
        self.rented_video = rented_video
        self.due_date = due_date


class VideoStore:
    """Manages a collection of videos and handles the rental/return process."""

    def __init__(self, videos: list[str]):
        """Initializes the store inventory."""
        all_videos = all(isinstance(video, Video) for video in videos)

        if not all_videos:
            raise ValueError("The video is not from our collection")

        self.videos = videos
        self.availability = {}

        for video in videos:
            self.availability[video.title] = True

        if len(videos) < 1 or len(videos) > 10:
            raise ValueError(
                "The video store must have a minimum or one video and no more than 10 videos")

    def find_video_by_title(self, video_name):
        """Searches for a video and returns its display title."""
        for video in self.videos:
            if video_name.lower() == video.title.lower():
                return video.display_title()

        raise ValueError(
            f"Could not find {video_name} in storage")

    def get_video_object_by_title(self, title):
        """Returns the actual Video object matching the title."""
        for video in self.videos:
            if title.lower() == video.title.lower():
                return video

    def is_available(self, title):
        """Checks if a video is currently in stock."""
        if isinstance(title, Video):
            title = title.title

        if self.availability[title] == True:
            return True
        raise KeyError(f"This {title} is unavailable at this moment of time")

    def rent_video(self, title: str, customer: Customer) -> Rental:
        """Processes a rental for a customer."""
        if customer.outstanding_fine > 50:
            raise Exception(
                "You've accrued a fine of more than £50, please pay it off first.")
        if self.availability[title] == False:
            raise Exception(f"{title} is already rented out")
        self.availability[title] = False

        due_date = datetime.now() + timedelta(days=14)

        video = self.get_video_object_by_title(title)
        return Rental(customer, video, due_date)

    def return_video(self, rental: Rental, return_date: str):
        """Processes the return of a rented video and applies late fines."""
        video = rental.rented_video
        if video.is_rewound == False:
            raise Exception("The rented video hasn't been rewound")
        self.availability[video.title] = True
        formatted_return_date = datetime.strptime(return_date, '%d/%m/%Y')
        return_date = formatted_return_date.date()

        if return_date > rental.due_date.date():
            rental.renting_customer.outstanding_fine += 10
            if video.year == datetime.now().year:
                rental.renting_customer.outstanding_fine += 5


class DVD(Video):
    """A modern alternative to VHS. Does not require rewinding."""

    def rental_price(self):
        """Returns a flat rate for DVD rentals (1200 pence)."""
        return 1200

    def watch(self):
        """Simulates watching; DVDs stay 'rewound' electronically."""
        self.is_rewound = False


class VendingMachine(VideoStore):
    """A smaller, automated version of the VideoStore."""

    def __init__(self, videos):
        """Initializes a machine with a strict limit of 1-5 videos."""
        super().__init__(videos)

        self.outstanding_fines = 0
        if not self.videos or len(self.videos) > 5:
            raise ValueError(
                "The vending machine must have between 1 and 5 videos")
