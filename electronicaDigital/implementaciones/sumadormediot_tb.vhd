
LIBRARY ieee;
USE ieee.std_logic_1164.ALL;
 
-- Uncomment the following library declaration if using
-- arithmetic functions with Signed or Unsigned values
--USE ieee.numeric_std.ALL;
 
ENTITY sumadormediot_tb IS
END sumadormediot_tb;
 
ARCHITECTURE behavior OF sumadormediot_tb IS 
 
    -- Component Declaration for the Unit Under Test (UUT)
 
    COMPONENT sumadormedio
    PORT(
         a : IN  std_logic;
         b : IN  std_logic;
         s : OUT  std_logic;
         cout : OUT  std_logic
        );
    END COMPONENT;
    

   --Inputs
   signal a : std_logic := '0';
   signal b : std_logic := '0';

 	--Outputs
   signal s : std_logic;
   signal cout : std_logic;
   
 
BEGIN
 
	-- Instantiate the Unit Under Test (UUT)
   uut: sumadormedio PORT MAP (
          a => a,
          b => b,
          s => s,
          cout => cout
        );


   -- Stimulus process
   stim_proc: process
   begin		
      -- hold reset state for 100 ns.
      wait for 100 ns;	
		b<='1';
      wait for 100 ns;
		a<='1';
		b<='0';
		 wait for 100 ns;

		 b<='1';
      -- insert stimulus here 

      wait;
   end process;

END;
