package book_manager;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import java.util.Random;

/**
 * BookManager 클래스의 두 search 함수의 성능을 테스트합니다.
 * searchBook() 메소드와 search_bs() 메소드의 실행 시간을 측정하고 비교.
 */

class BookManagerPerformanceTest {
    private BookManager bookManager;
    private Random random;
    
    /**
     * PerformanceTest를 위한 임시 책 100개 생
     */
    @BeforeEach
    void setUp() {
        bookManager = new BookManager();
        random = new Random();
        for (int i = 1; i <= 1000; i++) {
            bookManager.addBook(new Book(String.valueOf(i), "Title_" + i, "Author_" + i, i));
        }
    }
    
    /**
     * 두 Test 단계 모두 범위 내의 random number를 생성한 뒤 search를 진행
     * 총 100회씩 진행한 뒤 평균 시간을 출력하여 결과를 비교
     */

    @Test
    void testSearchBookPerformance() {
        long totalDuration = 0;
        int numberOfTests = 100;

        for (int i = 0; i < numberOfTests; i++) {
            String randomId = String.valueOf(random.nextInt(1000) + 1);
            long startTime = System.nanoTime();
            bookManager.searchBook(randomId);
            long endTime = System.nanoTime();
            long duration = endTime - startTime;

            totalDuration += duration;
        }

        long averageDuration = totalDuration / numberOfTests;
        System.out.println("searchBook() average duration: " + averageDuration);
    }

    @Test
    void testSearch_bsPerformance() {
        long totalDuration = 0;
        int numberOfTests = 10;

        for (int i = 0; i < numberOfTests; i++) {
            String randomId = String.valueOf(random.nextInt(1000) + 1);
            long startTime = System.nanoTime();
            bookManager.search_bs(randomId);
            long endTime = System.nanoTime();
            long duration = endTime - startTime;

            totalDuration += duration;
        }

        long averageDuration = totalDuration / numberOfTests;
        System.out.println("search_bs() average duration: " + averageDuration);
    }
}