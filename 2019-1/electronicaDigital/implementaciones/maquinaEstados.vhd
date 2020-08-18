----------------------------------------------------------------------------------
-- Company: 
-- Engineer: 
-- 
-- Create Date:    09:45:09 06/27/2019 
-- Design Name: 
-- Module Name:    maquinaEstados - Behavioral 
-- Project Name: 
-- Target Devices: 
-- Tool versions: 
-- Description: 
--
-- Dependencies: 
--
-- Revision: 
-- Revision 0.01 - File Created
-- Additional Comments: 
--
----------------------------------------------------------------------------------
library IEEE;
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity MaquinaDeDulces is
    Port ( m : in std_logic_vector (1 downto 0);
			  clk : in STD_LOGIC;
           boton : in  STD_LOGIC;
			  cambio : out  STD_LOGIC_VECTOR(2 downto 0);
           dulces : out  STD_LOGIC_VECTOR(1 downto 0)
			  );
end MaquinaDeDulces;

architecture Behavioral of MaquinaDeDulces is

type acumulado is (q0, q5, q10, q15, q20);
signal estado : acumulado := q0;
signal sumd: STD_LOGIC_VECTOR(1 downto 0) := (others => '0');
	
begin
process (clk) begin
		if rising_edge(clk) then
		
			case estado is
			
				when q0 =>
					if boton = '1' then
						cambio <= "000";
						dulces <= sumd;
						sumd <= "00";
					elsif sumd /= "11" then
						if m = "01" then
							estado <= q5;
						elsif m = "10" then
							estado <= q10;
						elsif m = "11" then
							estado <= q20;
						end if;
					end if;
				
				when q5 =>
					if boton = '1' then
						cambio <= "001";
						dulces <= sumd;
						sumd <= "00";
					elsif sumd /= "11" then
						if m = "01" then
							estado <= q10;
						elsif m = "10" then
							estado <= q15;
						elsif m = "11" then
							if sumd(0) = '1' then
								sumd <= "10";
							else
								sumd(0) <= '1';
							end if;
							estado <= q0;
						end if;
					end if;
					
				when q10 =>
					if boton = '1' then
						cambio <= "010";
						dulces <= sumd;
						sumd <="00";
					elsif sumd /= "11" then
						if m = "01" then
							estado <= q15;
						elsif m = "10" then
							estado <= q20;
						elsif m = "11" then
							if sumd(0) = '1' then
								sumd <= "10";
							else
								sumd(0) <= '1';
							end if;
							estado <= q5;
						end if;
					end if;
					
				when q15 =>
					if boton = '1' then
						cambio <= "011";
						dulces <= sumd;
						sumd <= "00";
					elsif sumd /= "11" then
						if m = "01" then
							estado <= q20;
						elsif m = "10" then
							if sumd(0) = '1' then
								sumd <= "10";
							else
								sumd(0) <= '1';
							end if;
							estado <= q0;
						elsif m = "11" then
							if sumd(0) = '1' then
								sumd <= "10";
							else
								sumd(0) <= '1';
							end if;
							estado <= q10;
						end if;
					end if;
					
				when q20 =>
					if boton = '1' then
						cambio <= "100";
						dulces <= sumd;
						sumd <= "00";
					elsif m = "01" then
						if sumd(0) = '1' then
								sumd <= "10";
							else
								sumd(0) <= '1';
							end if;
						estado <= q0;
					elsif m = "10" then
						if sumd(0) = '1' then
								sumd <= "10";
							else
								sumd(0) <= '1';
							end if;
						estado <= q5;
					elsif m = "11" then
						if sumd(0) = '1' then
								sumd <= "10";
							else
								sumd(0) <= '1';
							end if;
						estado <= q15;
					end if;
					
			end case;
		end if;
end process;

end Behavioral;

