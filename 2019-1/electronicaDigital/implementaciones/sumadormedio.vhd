----------------------
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;



entity sumadormedio is
    Port ( a : in  STD_LOGIC;
           b : in  STD_LOGIC;
           s : out  STD_LOGIC;
           cout : out  STD_LOGIC);
end sumadormedio;

architecture Behavioral of sumadormedio is

signal caso: std_logic_vector(1 downto 0):= "00";



begin
caso<= a&b;

process(caso)
begin
   
     
         case caso is
            when "00" => s<='0';cout<='0';
            when "01" => s<='1';cout<='0';
            when "10" => s<='1';cout<='0';
            when "11" => s<='0';cout<='1';
            when others => s<='0';cout<='0';
         end case;
     
end process;

				

end Behavioral;

