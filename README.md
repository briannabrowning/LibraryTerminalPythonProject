# Library Terminal Point of Sale


The Python code simulates a library management system, comprising classes for managing books and movies. The foundation of the system lies in the Media class, serving as the base class for any media item. Each media item, whether it's a book or a movie, inherits properties and methods from this base class. It primarily includes an initialization method to set the title and a string representation method to display information about the media.
Expanding upon the Media class, the Book class is introduced to represent books in the library. In addition to inheriting properties from the base class, it incorporates attributes such as authors, status, condition, and due date. The checkout and return_item methods enable the borrowing and returning of books, updating their status accordingly. Furthermore, a degrade_condition method facilitates the degradation of a book's condition over time, eventually leading to recycling.
Similarly, the Movie class inherits from the Media class and is tailored to handle movies in the library. It includes attributes like runtime, directors, and status, reflecting the essential details of a movie. Methods like checkout and return_item function analogously to their counterparts in the Book class, managing the borrowing and returning of movies.
To facilitate user interaction, the code implements several functions. display_media presents a list of media items, aiding users in browsing the library catalog. checkout_media allows users to borrow media items by specifying their titles. search_by_a_d and search_by_title offer users the ability to search for media items based on author/director names or title keywords, respectively. Finally, return_media enables users to return borrowed items, updating their status and condition as necessary.
The core interaction loop is governed by the main function. Upon execution, users are prompted to select between viewing the status of books, movies, or quitting the program. Based on the user's choice, they can explore the catalog, check out items, return borrowed items, or exit the system. This structured flow ensures a user-friendly experience, guiding users through various functionalities of the library management system seamlessly.
In summary, the provided Python code encapsulates a robust library management system, employing object-oriented principles to handle books and movies effectively. Its modular design, coupled with intuitive user interactions, makes it a versatile tool for managing and accessing media resources within a library setting.





