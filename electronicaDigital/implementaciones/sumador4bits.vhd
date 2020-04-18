----------------------------------------------
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;



entity sumador4bits is
    Port ( a : in  STD_LOGIC_VECTOR (3 downto 0);
           b : in  STD_LOGIC_VECTOR (3 downto 0);
           s : out  STD_LOGIC_VECTOR (3 downto 0);
           cout : out  STD_LOGIC);
end sumador4bits;

architecture Behavioral of sumador4bits is


	COMPONENT sumadormedio
	PORT(
		a : IN std_logic;
		b : IN std_logic;          
		s : OUT std_logic;
		cout : OUT std_logic
		);
	END COMPONENT;

	COMPONENT sumadorCompleto
	PORT(
		a : IN std_logic;
		b : IN std_logic;
		cin : IN std_logic;          
		s : OUT std_logic;
		cout : OUT std_logic
		);
	END COMPONENT;



signal c0: std_logic := '0';
signal c1 :std_logic := '0';
signal c2 :std_logic := '0';



begin
	Inst_sumadormedio: sumadormedio PORT MAP(
		a => a(0),
		b => b(0),
		s => s(0),
		cout => c0
	);

	Inst_sumadorCompleto_1: sumadorCompleto PORT MAP(
		a => a(1),
		b => b(1),
		cin => c0,
		s => s(1),
		cout => c1
	);


	Inst_sumadorCompleto_2: sumadorCompleto PORT MAP(
		a => a(2),
		b => b(2),
		cin => c1,
		s => s(2),
		cout => c2
	);
	
	Inst_sumadorCompleto_3: sumadorCompleto PORT MAP(
		a => a(3),
		b => b(3),
		cin => c2,
		s => s(3),
		cout => cout
	);




end Behavioral;

