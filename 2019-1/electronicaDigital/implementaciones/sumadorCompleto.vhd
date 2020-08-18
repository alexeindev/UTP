------------------
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;



entity sumadorCompleto is
    Port ( a : in  STD_LOGIC;
           b : in  STD_LOGIC;
           cin : in  STD_LOGIC;
           s : out  STD_LOGIC;
           cout : out  STD_LOGIC);
end sumadorCompleto;

architecture Behavioral of sumadorCompleto is

begin

cout<= (a and b) or ( (a xor b) and cin );
s<= (a xor b ) xor cin;

end Behavioral;

