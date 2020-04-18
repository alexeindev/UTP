LIBRARY ieee;
USE ieee.std_logic_1164.ALL;
 
-- Uncomment the following library declaration if using
-- arithmetic functions with Signed or Unsigned values
--USE ieee.numeric_std.ALL;
 
ENTITY simulacionDulces IS
END simulacionDulces;
 
ARCHITECTURE behavior OF simulacionDulces IS 
 
    -- Component Declaration for the Unit Under Test (UUT)
 
    COMPONENT MaquinaDeDulces
    PORT(
         m : IN  std_logic_vector(1 downto 0);
         clk : IN  std_logic;
         boton : IN  std_logic;
         cambio : OUT  std_logic_vector(2 downto 0);
         dulces : OUT  std_logic_vector(1 downto 0)
        );
    END COMPONENT;
    

   --Inputs
   signal m : std_logic_vector(1 downto 0) := "00";
   signal clk : std_logic := '0';
   signal boton : std_logic := '0';

 	--Outputs
   signal cambio : std_logic_vector(2 downto 0);
   signal dulces : std_logic_vector(1 downto 0);

   -- Clock period definitions
   constant clk_period : time := 10 ns;
 
BEGIN
 
	-- Instantiate the Unit Under Test (UUT)
   uut: MaquinaDeDulces PORT MAP (
          m => m,
          clk => clk,
          boton => boton,
          cambio => cambio,
          dulces => dulces
        );

   -- Clock process definitions
   clk_process :process
   begin
		clk <= '0';
		wait for clk_period/2;
		clk <= '1';
		wait for clk_period/2;
   end process;
 

   -- Stimulus process
   stim_proc: process
   begin		
      -- hold reset state for 100 ns.
      wait for 100 ns;	

      wait for clk_period*10;

      -- insert stimulus here 
		m <= "11";
		wait for 30 ns;
		m <= "10";
		wait for 10 ns;		
		m <= "00";	
		boton <= '1';		
		wait for 10 ns;			
		
		wait for 100 ns;	

		wait for 100 ns;	

		m <= "01";
		boton <= '1';
		wait for 10 ns;	
		
		
      wait;
   end process;

END;
