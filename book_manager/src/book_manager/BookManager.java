package book_manager;

import java.util.ArrayList;
import java.util.List;

/**
 * BookManager 클래스는 책 추가, 검색, 삭제 기능을 제공
 */
public class BookManager {
    private List<Book> books;

    /**
     * BookManager 생성자.
     * 책 리스트를 초기화
     */
    public BookManager() {
        books = new ArrayList<>();
    }

    /**
     * 새로운 책을 추가
     * 만약 동일한 ID를 가진 책이 이미 존재하면 추가하지 않음
     *
     * @param book - 추가할 책 객체
     * @return 추가 성공 여부, true - 새 책 추가 / false - 해당 아이디 책 이미 존재
     */
    public boolean addBook(Book book) {
        for (Book tmpBook : books) {
            if (tmpBook.getId().equals(book.getId())) {
                System.out.println("해당 ID(" + book.getId() + ")는 이미 존재합니다.");
                return false;
            }
        }
        books.add(book);
        System.out.println(book + "도서가 추가되었습니다.");
        return true;
    }
    
    /**
     * 주어진 ID에 해당하는 책을 검색
     * 검색 결과를 출력하고, 해당 책을 반환
     *
     * @param id - 검색할 책의 ID
     * @return 검색 성공한 경우 - 검색된 책 객체 / null - 책을 찾지 못한 경우
     */
    public Book searchBook(String id) {
        boolean found = false;
        System.out.println("검색 결과: ");
        for (Book tmpBook : books) {
            if (tmpBook.getId().equals(id)) {
                System.out.println(tmpBook);
                found = true;
                return tmpBook;
            }
        }
        if (!found) {
            System.out.println("검색된 도서가 없습니다.");
        }
        return null;
    }

    /**
     * 주어진 ID에 해당하는 책을 삭제
     * 삭제 결과를 출력하고, 삭제 성공 여부를 반환
     *
     * @param id - 삭제할 책의 ID
     * @return 책 삭제 성공 여부, true - 삭제 성공 / false - 해당 ID의 책이 없음.
     */
    public boolean removeBook(String id) {
        for (Book tmpBook : books) {
            if (tmpBook.getId().equals(id)) {
                books.remove(tmpBook);
                System.out.println(tmpBook + "도서를 삭제하였습니다.");
                return true;
            }
        }
        System.out.println("해당 ID(" + id + ")의 도서를 찾을 수 없습니다.");
        return false;
    }
}
