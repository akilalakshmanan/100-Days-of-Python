<?php
    if ( isset( $_POST['login'] ) ) 
	{
		$servername = "localhost";
		$username = "root";
		$password = "";
		$dbname = "empowher";
       
		// Create connection
        $conn = new mysqli($servername, $username, $password, $dbname);
        
		// Check connection
		if ($conn->connect_error) {
		  die("Connection failed: " . $conn->connect_error);
        }
        

		$emailid = $_POST['emailid']; 
        $pwd = $_POST['pwd']; 
        $sql_stmt = "SELECT E_mailId,Password from register";
        
        
        $result = $conn->query($sql_stmt);
        $login_success = -1;
        if ($result->num_rows > 0) { //checking whether no. of rows greater then 0
            // output data of each row
            while($row = $result->fetch_assoc()) { // getting each object values into $rows
           
                if(0 == strcmp($emailid,$row["E_mailId"])){ // checking email given == db value
                    if(0 == strcmp($pwd,$row["Password"])){ // checking pwd with given pwd
                        
                    echo '<script language="javascript">';
                    echo 'alert("Successfully signed in... Welcome :) ");';
                    echo 'window.location.href="index.html";';
                    echo '</script>';
                   
                    $login_success = 0; // this will specify whether user is given correct values
                    break; // breaking if matched
                    }
                }

                //echo "Name: " . $row["E_mailId"]. " " . $row["Password"]. "<br>";
            }
        } else {
        echo "0 results";
        }

        if($login_success == -1){ // if login_success == -1 the login has failed..
            echo '<script language="javascript">';
            echo 'alert("Login Failed. Incorrect Email or Password");';
            echo 'window.location.href="failed.html";';
            echo '</script>';
            
        }
       

		$conn->close();
	}
?>

