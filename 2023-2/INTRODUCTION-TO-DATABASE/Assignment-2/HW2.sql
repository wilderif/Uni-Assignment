-- 데이터베이스 생성 및 지정
create database IF NOT EXISTS hotel_booking;
use hotel_booking;
alter database hotel_booking default character set utf8mb4;

set foreign_key_checks = 0;    			-- 외래키 체크하지 않는 것으로 설정
drop table IF EXISTS hotel cascade;   				-- 기존 hotel 테이블 제거
drop table IF EXISTS hotelier cascade;   			-- 기존 hotelier 테이블 제거
drop table IF EXISTS hotel_room cascade;   			-- 기존 hotel_room 테이블 제거
drop table IF EXISTS customer cascade;   			-- 기존 customer 테이블 제거
drop table IF EXISTS booking cascade;   			-- 기존 booking 테이블 제거 
drop table IF EXISTS stay_information cascade; 		-- 기존 stay_information 테이블 제거 
drop view IF EXISTS hongik_hotel_customers cascade; -- 기존 hongik_hotel_customers 뷰 제거
set foreign_key_checks = 1;   			-- 외래키 체크하는 것으로 설정

-- (1)  테이블 생성 

-- hotel 테이블 생성
create table hotel (
	HID varchar(20) not null,
    호텔이름 varchar(10),
    호텔주소 varchar(20),
    호텔전화번호 varchar(20),
    primary key (HID)
);

-- hotelier 테이블 생성
-- hotelier는 호텔과 존재종속 관계가 아니기 때문에 호텔이 없어지거나 휴직을 하는 등의 상황에서도 정보가 유지될 수 있다.
-- 따라서 HID는 null 가질 수 있고, on delete cascade하지 않음
create table hotelier (
	HLID varchar(20) not null,
    호텔리어이름 varchar(10),
    HID varchar(20),
    primary key (HLID),
    foreign key (HID) references hotel(HID)
);

-- hotel_room 테이블 생성
create table hotel_room (
	HID varchar(20) not null,
    호실 varchar(10) not null,
    가격 int,
    primary key (HID, 호실),
    foreign key (HID) references hotel(HID) on delete cascade
);

-- customer 테이블 생성
create table customer (
	CID varchar(20) not null,
    고객이름 varchar(10),
    고객전화번호 varchar(20),
    primary key (CID)
);

-- booking 테이블 생성
create table booking (
	CID varchar(20) not null,
    HID varchar(20) not null,
    호실 varchar(10) not null,
    예약체크인날짜 date,
    예약체크아웃날짜 date,
    primary key (CID, HID, 호실),
    foreign key (CID) references customer(CID) on delete cascade,
    foreign key (HID, 호실) references hotel_room(HID, 호실) on delete cascade 
);

-- stay_information 테이블 생성
create table stay_information (
	CID varchar(20) not null,
    HID varchar(20) not null,
    호실 varchar(10) not null,
    체크인날짜 date not null,
    체크아웃날짜 date,
    primary key (CID, HID, 호실, 체크인날짜),
	foreign key (CID) references customer(CID) on delete cascade,
    foreign key (HID, 호실) references hotel_room(HID, 호실) on delete cascade 
);


-- (2)  데이터 삽입

-- hotel 테이블 데이터 삽입
insert
into hotel
values('H001', '홍익호텔', '마포구 상수동', '02-320-1234');

insert
into hotel
values('H002', '중앙호텔', '동작구 흑석동', '02-850-1234');

insert
into hotel
values('H003', '건국호텔', '광진구 자양동', '02-415-1234');

select *
from hotel;

-- hotelier 테이블 데이터 삽입
insert
into hotelier
values('HL001', 'KMS', 'H001');

insert
into hotelier
values('HL002', 'LED', 'H001');

insert
into hotelier
values('HL003', 'YHD', 'H002');

insert
into hotelier
values('HL004', 'KKT', 'H002');

insert
into hotelier
values('HL005', 'CPC', 'H003');

insert
into hotelier
values('HL006', 'LSY', 'H003');

select *
from hotelier;

-- hotel_room 테이블 데이터 삽입
insert
into hotel_room
values('H001', '01', '1400');

insert
into hotel_room
values('H001', '02', '1200');

insert
into hotel_room
values('H001', '03', '700');

insert
into hotel_room
values('H002', '01', '1900');

insert
into hotel_room
values('H002', '02', '1000');

insert
into hotel_room
values('H002', '03', '1300');

insert
into hotel_room
values('H002', '04', '1600');

insert
into hotel_room
values('H003', '01', '900');

insert
into hotel_room
values('H003', '02', '1100');

select *
from hotel_room;

-- customer 테이블 데이터 삽입
insert
into customer
values('C001', 'PDN', '010-3304-6302');

insert
into customer
values('C002', 'KYS', '010-7323-3789');

insert
into customer
values('C003', 'YDJ', '010-2628-7436');

insert
into customer
values('C004', 'KSM', '010-2299-7827');

insert
into customer
values('C005', 'PJH', '010-3157-2501');

insert
into customer
values('C006', 'HBC', '010-2936-5427');

insert
into customer
values('C007', 'KCY', '010-7119-6732');

insert
into customer
values('C008', 'PYS', '010-2523-9738');

select *
from customer;

-- booking 테이블 데이터 삽입
insert
into booking
values('C001', 'H001', '01', '2023/07/16', '2023/07/28');

insert
into booking
values('C002', 'H001', '02', '2023/07/21', '2023/07/22');

insert
into booking
values('C001', 'H002', '01', '2023/08/16', '2023/08/18');

insert
into booking
values('C005', 'H002', '01', '2023/09/06', '2023/09/09');

insert
into booking
values('C005', 'H002', '02', '2023/09/10', '2023/09/18');

insert
into booking
values('C003', 'H002', '02', '2023/09/14', '2023/10/17');

insert
into booking
values('C002', 'H002', '03', '2023/10/16', '2023/10/18');

insert
into booking
values('C008', 'H003', '01', '2023/10/22 ', '2023/10/26');

insert
into booking
values('C004', 'H003', '01', '2023/10/28', '2023/11/02');

insert
into booking
values('C003', 'H003', '02', '2023/10/29', '2023/11/03');

select *
from booking;

-- stay_information 테이블 데이터 삽입
insert
into stay_information
values('C002', 'H002', '01', '2021/07/16', '2021/07/20');

insert
into stay_information
values('C001', 'H003', '02', '2021/07/21', '2021/07/25');

insert
into stay_information
values('C001', 'H001', '01', '2021/08/16', '2021/08/28');

insert
into stay_information
values('C004', 'H002', '02', '2021/09/06', '2021/09/18');

insert
into stay_information
values('C001', 'H002', '02', '2021/09/10', '2021/09/17');

insert
into stay_information
values('C003', 'H002', '02', '2021/09/14', '2021/09/21');

insert
into stay_information
values('C002', 'H001', '03', '2022/10/15', '2022/10/24');

insert
into stay_information
values('C005', 'H003', '01', '2022/10/19', '2022/10/26');

insert
into stay_information
values('C004', 'H002', '01', '2022/10/22', '2022/10/26');

insert
into stay_information
values('C005', 'H003', '02', '2022/10/29', '2022/11/01');

select *
from stay_information;


-- (3) 1)
select "1)";       -- 문제 번호 출력하기

select * 
from hotel;

select *
from hotelier;

select *
from hotel_room;

select *
from customer;

select *
from booking;

select *
from stay_information;

-- (3) 2)
select "2)";       -- 문제 번호 출력하기

select HLID, 호텔리어이름
from hotelier
where HID = 'H001';

-- (3) 3)
select "3)";       -- 문제 번호 출력하기

select customer.CID, stay_information.HID, sum(datediff(stay_information.체크아웃날짜, stay_information.체크인날짜)) as '투숙일 수 합'
from stay_information, customer
where stay_information.CID = customer.CID
group by stay_information.CID, stay_information.HID;

-- (3) 4)
select "4)";       -- 문제 번호 출력하기

select customer.고객이름, hotel.호텔이름
from booking, customer, hotel
where datediff(booking.예약체크아웃날짜, booking.예약체크인날짜) < 4
		and booking.CID = customer.CID 
        and booking.HID = hotel.HID;

-- (3) 5)
select "5)";       -- 문제 번호 출력하기

select sum(datediff(체크아웃날짜, 체크인날짜)) as '투숙한 총일 수'
from stay_information
where CID = 'C001';

-- (3) 6)
select "6)";       -- 문제 번호 출력하기

select *
from hotel_room
where 가격 >= 1300
order by HID desc, 호실 asc;

-- (3) 7)
select "7)";       -- 문제 번호 출력하기

select hotel.호텔이름, hotel.호텔전화번호
from stay_information, hotel
where stay_information.체크인날짜 = (select min(체크인날짜)
								  from stay_information)
	and stay_information.HID = hotel.HID;

-- (3) 8)
select "8)";       -- 문제 번호 출력하기

select distinct customer.고객이름
from customer, booking, stay_information
where booking.HID = 'H003'
	and booking.CID = customer.CID;
    
-- (3) 9)
select "9)";       -- 문제 번호 출력하기

select distinct hotel.호텔이름
from hotel, stay_information
where hotel.HID = stay_information.HID
	and stay_information.HID = (select HID
								from stay_information
                                where 체크인날짜 >= '2021/01/01'
									and 체크인날짜 < '2022/01/01'
								group by HID having count(*) >= 2);

-- (3) 10)
select "10)";       -- 문제 번호 출력하기

select distinct customer.고객이름, customer.고객전화번호
from customer, stay_information, hotel, booking
where stay_information.체크인날짜 < '2022/08/30'
	and stay_information.CID = customer.CID
	and hotel.호텔주소 like '%흑석동'
    and booking.HID = hotel.HID
    and booking.CID = customer.CID;

-- (3) 11)
select "11)";       -- 문제 번호 출력하기

select distinct customer.고객이름
from customer, booking, stay_information
where customer.CID = booking.CID
	and booking.HID = 'H001'
    and booking.CID in (select CID
						from booking
                        where HID = 'H002');

-- (3) 12)
select "12)";       -- 문제 번호 출력하기

select hotel.HID, count(*) as '총 예약 수'
from hotel, booking
where hotel.HID = booking.HID
group by hotel.HID;

select hotel.HID, count(*) as '총 투숙 수'
from hotel, stay_information
where hotel.HID = stay_information.HID
group by hotel.HID;

-- (3) 13)
select "13)";       -- 문제 번호 출력하기

update hotel_room
set 가격 = 가격 + 100
where (HID, 호실) in (select HID, 호실
			  from booking
              where CID = 'C002');

select *
from hotel_room;

-- (3) 14)
select "14)";       -- 문제 번호 출력하기

delete
from hotelier
where HID in (select HID
			  from hotel
              where 호텔이름 = '중앙호텔');

select *
from hotelier;

-- (3)  15)
select "15)";       -- 문제 번호 출력하기

create view hongik_hotel_customers
as select customer.CID, customer.고객이름, customer.고객전화번호
	from customer, stay_information, hotel
    where hotel.호텔이름 = '홍익호텔'
		and stay_information.HID = hotel.HID
        and stay_information.CID = customer.CID;

select *
from hongik_hotel_customers;


set foreign_key_checks = 0;    			-- 외래키 체크하지 않는 것으로 설정
drop table IF EXISTS hotel cascade;   				-- 기존 hotel 테이블 제거
drop table IF EXISTS hotelier cascade;   			-- 기존 hotelier 테이블 제거
drop table IF EXISTS hotel_room cascade;   			-- 기존 hotel_room 테이블 제거
drop table IF EXISTS customer cascade;   			-- 기존 customer 테이블 제거
drop table IF EXISTS booking cascade;   			-- 기존 booking 테이블 제거 
drop table IF EXISTS stay_information cascade; 		-- 기존 stay_information 테이블 제거 
drop view IF EXISTS hongik_hotel_customers cascade; -- 기존 hongik_hotel_customers 뷰 제거
set foreign_key_checks = 1;   			-- 외래키 체크하는 것으로 설정
