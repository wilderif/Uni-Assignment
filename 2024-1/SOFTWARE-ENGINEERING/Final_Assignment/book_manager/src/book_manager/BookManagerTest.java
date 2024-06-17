package book_manager;

import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

class BookManagerTest {
    private BookManager bookManager;

    @BeforeEach
    void setUp() {
        bookManager = new BookManager();
        bookManager.addBook(new Book("1", "자바 기초", "Jane", 2021));
        bookManager.addBook(new Book("2", "소프트웨어 공학", "Tom", 2014));
        bookManager.addBook(new Book("3", "분산 컴퓨팅", "Yoon", 2024));
    }

    @Test
    
    void testAddBook() {
        Book newBook = new Book("4", "알고리즘", "Alice", 2023);
        assertTrue(bookManager.addBook(newBook));
        assertFalse(bookManager.addBook(new Book("1", "자바 기초", "Jane", 2021)));
        System.out.println("testAddBook passed");
    }

    
    @Test
    void testSearchBook() {
        assertNotNull(bookManager.searchBook("1"));
        assertNull(bookManager.searchBook("5"));
        System.out.println("testSearchBook passed");
    }
    
    @Test
    void testSearch_bs() {
        assertNotNull(bookManager.search_bs("1"));
        assertNull(bookManager.search_bs("5"));
        System.out.println("testSearch_bs passed");
    }

    @Test
    void testRemoveBook() {
        assertTrue(bookManager.removeBook("1"));
        assertFalse(bookManager.removeBook("1"));
        assertFalse(bookManager.removeBook("5"));
        System.out.println("testRemoveBook passed");
    }
}
