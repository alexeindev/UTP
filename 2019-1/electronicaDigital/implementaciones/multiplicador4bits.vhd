
----------------------------------------------------------------------------------
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;



entity multiplicador4bits is
    Port ( a : in  STD_LOGIC_VECTOR (3 downto 0);
           b : in  STD_LOGIC_VECTOR (3 downto 0);
           
           r : out  STD_LOGIC_VECTOR (7 downto 0));
end multiplicador4bits;


architecture Behavioral of multiplicador4bits is
	
COMPONENT sumadorCompleto
	PORT(
		a : IN std_logic;
		b : IN std_logic;
		cin : IN std_logic;          
		s : OUT std_logic;
		cout : OUT std_logic
		);
	END COMPONENT;

signal c : std_logic_vector (14 downto 0 );
signal carry: std_logic_vector( 10  downto 0);
signal e: std_logic_vector ( 5 downto 0);

begin

r(0) <= a(0)and b(0);

c(0)<= a(1)and b(0);
c(1)<= a(0)and b(1);

c(2)<= a(2)and b(0);
c(3)<= a(1)and b(1);
c(4)<= a(3)and b(0);
c(5)<= a(2)and b(1);
c(6)<= a(3)and b(1);
c(7)<= a(0)and b(2);
c(8)<= a(1)and b(2);
c(9)<= a(2)and b(2);
c(10)<= a(3)and b(2);
c(11)<= a(0)and b(3);
c(12)<= a(1)and b(3);
c(13)<= a(2)and b(3);
c(14)<= a(3)and b(3);

	Inst_sumadorCompleto_0: sumadorCompleto PORT MAP(
		a => c(1),
		b => c(0),
		cin => '0',
		s => r(1) , 
		cout =>  carry(0)
	);

	Inst_sumadorCompleto_1: sumadorCompleto PORT MAP(
		a => c(3) ,
		b => c(2),
		cin => carry(0),
		s => e(0),
		cout =>carry(1) 
	);

	Inst_sumadorCompleto_2: sumadorCompleto PORT MAP(
		a => c(5),
		b => c(4),
		cin => carry(1),
		s => e(1),
		cout =>carry(2) 
	);

	Inst_sumadorCompleto_3: sumadorCompleto PORT MAP(
		a => c(6),
		b => '0',
		cin => carry(2),
		s => e(2),
		cout => carry(3)
	);

	Inst_sumadorCompleto_4: sumadorCompleto PORT MAP(
		a => c(7),
		b => e(0),
		cin => '0',
		s => r(2),
		cout => carry(4)
	);

	Inst_sumadorCompleto_5: sumadorCompleto PORT MAP(
		a => c(8),
		b => e(1),
		cin =>carry(4) ,
		s => e(3),
		cout => carry(5)
	);

	Inst_sumadorCompleto_6: sumadorCompleto PORT MAP(
		a => c(9),
		b => e(2),
		cin => carry(5),
		s => e(4),
		cout =>carry(6) 
	);

	Inst_sumadorCompleto_7: sumadorCompleto PORT MAP(
		a => c(10),
		b => carry(3),
		cin => carry(6),
		s => e(5),
		cout => carry(7)
	);

	Inst_sumadorCompleto_8: sumadorCompleto PORT MAP(
		a =>c(11),
		b => e(3),
		cin => '0',
		s => r(3),
		cout => carry(8)
	);

	Inst_sumadorCompleto_9: sumadorCompleto PORT MAP(
		a => c(12),
		b => e(4),
		cin => carry(8),
		s => r(4),
		cout => carry(9)
	);

	Inst_sumadorCompleto_10: sumadorCompleto PORT MAP(
		a => c(13),
		b => e(5),
		cin => carry(9),
		s => r(5),
		cout =>carry(10) 
	);

	Inst_sumadorCompleto_11: sumadorCompleto PORT MAP(
		a => c(14),
		b => carry(7),
		cin => carry(10),
		s => r(6),
		cout => r(7)
	);






end Behavioral;

