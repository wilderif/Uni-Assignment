import pymysql


# instruction group 1 - 공통 메뉴

# 1 1 - 회원가입
# 함수 이름 : sql_insert_customer
# 기능 : 파일로부터 관리자와 고객 정보를 입력 받아, customer table에 레코드를 삽입
# 반환값 : 없음
# 전달인자 : 없음
def sql_insert_customer():
    input_line = list(input_file.readline().strip().split())
    input_cid = input_line[0]
    input_cname = input_line[1]
    input_phone_number = input_line[2]

    # file 출력
    output_file.write("1.1. 회원가입\n")
    output_file.write(f"> {input_cid} {input_cname} {input_phone_number}\n")

    # customer table에 insert 실행 및 예외처리
    try:
        cursor.execute(f"""
            insert
            into customer
            values ('{input_cid}', '{input_cname}', '{input_phone_number}')""")
    except Exception as error:
        output_file.write("> " + str(error) + '\n')

    return None


# 1 2 - 종료
# 함수 이름 : exit_program
# 기능 : 프로그램 종료 output.txt에 출력
# 반환값 : 없음
# 전달인자 : 없음
def exit_program():
    # file 출력
    output_file.write("1.2. 종료")

    return None


# instruction group 2 - 고객 메뉴

# 2 1 - 로그인
# 함수 이름 : customer_login
# 기능 : 파일로부터 고객 ID를 입력 받아, do_task() 함수의 current_id를 로그인한 ID로 변경
# 반환값 : 가입한 ID인 경우 ID return 후 do_task() 함수의 current_id 변경, 가입하지 않은 ID인 경우 return None
# 전달인자 : 없음
def customer_login():
    input_line = input_file.readline().strip()

    # file 출력
    output_file.write("2.1. 로그인\n")
    output_file.write("> " + input_line + '\n')

    # customer table에서 CID 목록 가져오기
    cursor.execute("""
        select CID
        from customer""")
    cid_list = cursor.fetchall()

    # cid_list에 login 하려는 ID가 있으면 ID return, 없다면 예외 처리
    for row in cid_list:
        if row[0] == input_line:
            return input_line
    else:
        output_file.write("> 가입하지 않은 ID입니다.\n")
        return None


# 2 2 - 호텔방 예약
# 함수 이름 : sql_insert_booking
# 기능 : 파일로부터 속성들을 입력받아, booking table에 레코드 삽입
# 반환값 : 없음
# 전달인자 : do_task() 함수의 current_id
def sql_insert_booking(login_cid):
    input_line = list(input_file.readline().strip().split())
    input_hid = input_line[0]
    input_room_number = input_line[1]
    input_checkin_date = input_line[2]
    input_checkout_date = input_line[3]

    # file 출력
    output_file.write("2.2. 호텔방 예약\n")
    output_file.write(f"> {input_hid} {input_room_number} {input_checkin_date} {input_checkout_date}\n")

    # booking table에 insert 실행 및 예외처리
    try:
        cursor.execute(f"""
            insert
            into booking
            values ('{login_cid}', '{input_hid}', '{input_room_number}', '{input_checkin_date}', '{input_checkout_date}')""")
    except Exception as error:
        output_file.write("> " + str(error) + '\n')

    return None


# 2 3 - 호텔방 예약 조회
# 함수 이름 : sql_select_booking
# 기능 : 로그인한 고객 ID에 해당하는 booking table의 레코드를 검색하여, output file에 입력
# 반환값 : 없음
# 전달인자 : do_task() 함수의 current_id
def sql_select_booking(login_cid):
    # 로그인한 고객 ID로 예약 정보 가져와서 booking_list에 저장
    cursor.execute(f"""
        select HID, 호실, 예약체크인날짜, 예약체크아웃날짜
        from booking
        where CID = '{login_cid}'""")

    booking_list = cursor.fetchall()

    # file 출력
    output_file.write("2.3. 호텔방 예약 조회\n")
    if len(booking_list) == 0:  # 출력 레코드가 없을 떄 출력
        output_file.write(">\n")
    else:
        for booking in booking_list:
            hid = booking[0]
            room_number = booking[1]
            # 출력 형식 '-' -> '/'
            checkin_date = str(booking[2]).replace('-', '/')
            checkout_date = str(booking[3]).replace('-', '/')
            output_file.write(f"> {hid} {room_number} {checkin_date} {checkout_date}\n")

    return None


# 2 4 - 호텔방 예약 취소
# 함수 이름 : sql_delete_booking
# 기능 : 파일로부터 속성들을 입력받아, booking table에 레코드 삭제
# 반환값 : 없음
# 전달인자 : do_task() 함수의 current_id
def sql_delete_booking(login_cid):
    input_line = list(input_file.readline().strip().split())
    input_hid = input_line[0]
    input_room_number = input_line[1]

    # booking table에 delete 실행 및 예외처리
    try:
        cursor.execute(f"""
            delete
            from booking
            where CID = '{login_cid}' and HID = '{input_hid}' and 호실 = '{input_room_number}'""")
    except Exception as error:
        output_file.write("> " + str(error) + '\n')

    # file 출력
    output_file.write("2.4. 호텔방 예약 취소\n")
    output_file.write(f"> {input_hid} {input_room_number}\n")

    return None


# 2 5 - 로그아웃
# 함수 이름 : customer_logout
# 기능 : 로그인한 ID 로그아웃 (do_task() 함수의 current_id None으로 변경)
# 반환값 : 없음
# 전달인자 : do_task() 함수의 current_id
def customer_logout(login_cid):
    # file 출력
    output_file.write("2.5. 로그아웃\n")
    output_file.write("> " + login_cid + '\n')

    return None


# instruction group 3 - 관리자 메뉴

# 3 1 - 로그인
# 함수 이름 : admin_login
# 기능 : 파일로부터 관리자 ID를 입력 받아, 관리자 ID(admin) 인지 확인한 후, do_task() 함수의 current_id를 관리자 ID로 변경
# 반환값 : 관리자 ID인 경우 ID return 후 do_task() 함수의 current_id 변경, 가입하지 않은 ID인 경우 return None
# 전달인자 : 없음
def admin_login():
    input_line = input_file.readline().strip()

    # file 출력
    output_file.write("3.1. 로그인\n")
    output_file.write("> " + input_line + '\n')

    # 'admin'으로 로그인 하지 않은 경우 함수 종료
    if input_line != "admin":
        output_file.write("> 관리자 ID가 아닙니다.\n")
        return None

    # customer table에서 CID 목록 가져오기
    cursor.execute("""
        select CID
        from customer""")
    cid_list = cursor.fetchall()

    # cid_list에 login 하려는 ID가 있으면 ID return, 없다면 예외 처리
    for row in cid_list:
        if row[0] == input_line:
            return input_line
    else:
        output_file.write("> 가입하지 않은 ID입니다.\n")
        return None


# 3 2 - 호텔 정보 등록
# 함수 이름 : sql_insert_hotel
# 기능 : 로그인한 ID가 관리자 ID인지 확인 후, 파일로부터 속성들을 입력받아, hotel table에 레코드 삽입
# 반환값 : 없음
# 전달인자 : do_task() 함수의 current_id
def sql_insert_hotel(login_id):
    # 로그인한 ID가 관리자 ID인지 확인
    if login_id != "admin":
        output_file.write("> 관리자 ID가 아닙니다.\n")
        return None

    input_line = list(input_file.readline().strip().split())
    input_hid = input_line[0]
    input_hname = input_line[1]
    input_address = input_line[2]

    # file 출력
    output_file.write("3.2. 호텔 정보 등록\n")
    output_file.write(f"> {input_hid} {input_hname} {input_address}\n")

    # hotel table에 insert 실행 및 예외처리
    try:
        cursor.execute(f"""
            insert
            into hotel
            values ('{input_hid}', '{input_hname}', '{input_address}')""")
    except Exception as error:
        output_file.write("> " + str(error) + '\n')

    return None


# 3 3 - 호텔방 정보 등록
# 함수 이름 : sql_insert_hotel_room
# 기능 : 로그인한 ID가 관리자 ID인지 확인 후, 파일로부터 속성들을 입력받아, hotel_room table에 레코드 삽입
# 반환값 : 없음
# 전달인자 : do_task() 함수의 current_id
def sql_insert_hotel_room(login_id):
    # 로그인한 ID가 관리자 ID인지 확인
    if login_id != "admin":
        output_file.write("> 관리자 ID가 아닙니다.\n")
        return None

    input_line = list(input_file.readline().strip().split())
    input_hid = input_line[0]
    input_room_number = input_line[1]
    input_price = input_line[2]

    # file 출력
    output_file.write("3.3. 호텔방 정보 등록\n")
    output_file.write(f"> {input_hid} {input_room_number} {input_price}\n")

    # hotel_room table에 insert 실행 및 예외처리
    try:
        cursor.execute(f"""
            insert
            into hotel_room
            values ('{input_hid}', '{input_room_number}', '{input_price}')""")
    except Exception as error:
        output_file.write("> " + str(error) + '\n')

    return None


# 3 4 - 예약 내역 조회
# 함수 이름 : sql_select_all_booking
# 기능 : 로그인한 ID가 관리자 ID인지 확인 후, booking table의 모든 레코드를 검색하여, output file에 입력
# 반환값 : 없음
# 전달인자 : do_task() 함수의 current_id
def sql_select_all_booking(login_id):
    # 로그인한 ID가 관리자 ID인지 확인
    if login_id != "admin":
        output_file.write("> 관리자 ID가 아닙니다.\n")
        return None

    cursor.execute("""
        select *
        from booking""")
    booking_list = cursor.fetchall()

    # file 출력
    output_file.write("3.4. 예약 내역 조회\n")
    # 출력 레코드가 없을 떄 출력
    if len(booking_list) == 0:
        output_file.write(">\n")
    else:
        for booking in booking_list:
            # customer 정보
            cid = booking[0]
            cursor.execute(f"""
                select 고객이름
                from customer
                where CID = '{cid}'""")
            cname = cursor.fetchall()[0][0]
            # hotel 정보
            hid = booking[1]
            cursor.execute(f"""
                select 호텔이름, 호텔주소
                from hotel
                where HID = '{hid}'""")
            hotel_information = cursor.fetchall()
            hname = hotel_information[0][0]
            address = hotel_information[0][1]
            # hotel_room 정보
            room_number = booking[2]
            cursor.execute(f"""
                select 가격
                from hotel_room
                where HID = '{hid}' and 호실 = '{room_number}'""")
            price = cursor.fetchall()[0][0]
            # booking 정보 및 출력 형식 '-' -> '/'
            checkin_date = str(booking[3]).replace('-', '/')
            checkout_date = str(booking[4]).replace('-', '/')
            output_file.write(f"> {cid} {cname} {hid} {hname} {address} {room_number} {price} {checkin_date} {checkout_date}\n")

    return None


# 3 5 - 로그아웃
# 함수 이름 : admin_logout
# 기능 : 로그인한 ID 로그아웃 (do_task() 함수의 current_id None으로 변경)
# 반환값 : 없음
# 전달인자 : do_task() 함수의 current_id
def admin_logout(login_id):
    # file 출력
    output_file.write("3.5. 로그아웃\n")
    output_file.write("> " + login_id + '\n')

    return None


# instruction 실행

# 함수 이름 : do_task
# 기능 : 종료 메뉴(1 2)가 입력되기 전까지 반복, 종료 메뉴가 입력되면 return None으로 함수 종료, current_id 변수로 로그인한 ID정보 유지
# 반환값 : 없음
# 전달인자 : 없음
def do_task():
    # current_id 변수로 로그인한 ID정보 유지
    current_id = None

    # 종료 메뉴(1 2)가 입력되기 전까지 반복함
    while True:
        # 입력 파일에서 메뉴 숫자 2개 읽기
        inst = list(map(int, input_file.readline().strip().split()))

        # 메뉴 파싱을 위한 level 구분
        inst_level_1 = int(inst[0])
        inst_level_2 = int(inst[1])

        # 메뉴 구분 및 해당 연산 수행
        if inst_level_1 == 1:
            if inst_level_2 == 1:
                sql_insert_customer()
            elif inst_level_2 == 2:
                exit_program()
                return None
        elif inst_level_1 == 2:
            if inst_level_2 == 1:
                current_id = customer_login()
            elif inst_level_2 == 2:
                sql_insert_booking(current_id)
            elif inst_level_2 == 3:
                sql_select_booking(current_id)
            elif inst_level_2 == 4:
                sql_delete_booking(current_id)
            elif inst_level_2 == 5:
                customer_logout(current_id)
                current_id = None
        elif inst_level_1 == 3:
            if inst_level_2 == 1:
                current_id = admin_login()
            elif inst_level_2 == 2:
                sql_insert_hotel(current_id)
            elif inst_level_2 == 3:
                sql_insert_hotel_room(current_id)
            elif inst_level_2 == 4:
                sql_select_all_booking(current_id)
            elif inst_level_2 == 5:
                admin_logout(current_id)
                current_id = None


# main 함수 부분
if __name__ == "__main__":
    # mysql connection
    conn = pymysql.connect(host=,
                           user=,
                           password=,
                           db='hotel_booking',
                           charset='utf8mb4')

    cursor = conn.cursor()

    # 기존 table 삭제
    cursor.execute("set foreign_key_checks = 0")
    cursor.execute("drop table if exists hotel cascade")
    cursor.execute("drop table if exists hotel_room cascade")
    cursor.execute("drop table if exists customer cascade")
    cursor.execute("drop table if exists booking cascade")
    cursor.execute("set foreign_key_checks = 1")

    # hotel table 생성
    cursor.execute("""
        create table hotel (
            HID varchar(30) not null,
            호텔이름 varchar(30),
            호텔주소 varchar(30),
            primary key (HID))""")

    # hotel_room table 생성
    cursor.execute("""
        create table hotel_room(
            HID varchar(30) not null,
            호실 varchar(30) not null,
            가격 int,
            primary key (HID, 호실),
            foreign key (HID) references hotel(HID))""")

    # customer table 생성
    cursor.execute("""
        create table customer(
            CID varchar(30) not null,
            고객이름 varchar(30),
            고객전화번호 varchar(30),
            primary key (CID))""")

    # booking table 생성
    cursor.execute("""
        create table booking (
            CID varchar(30) not null,
            HID varchar(30) not null,
            호실 varchar(30) not null,
            예약체크인날짜 date,
            예약체크아웃날짜 date,
            primary key (CID, HID, 호실),
            foreign key (CID) references customer(CID),
            foreign key (HID, 호실) references hotel_room(HID, 호실))""")

    # file 열기
    input_file = open("input.txt", "r", encoding="UTF-8")
    output_file = open("output.txt", "w")

    do_task()

    # file 닫기
    input_file.close()
    output_file.close()

    # connection 종료
    conn.close()
