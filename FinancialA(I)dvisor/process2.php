
<?php

    /*
    $servername = "localhost";
    $username = "root";
    $password = "";
    $dbname = "mydb";
    

    // Create connection
    $connection = mysqli_connect($servername, 
        $username, $password, $dbname);
    
    // Check connection

    
    if (!$connection) { 
        die("Connection failed: ".mysqli_connection_error());
    }
    echo "Connected! <br>";

    */

    echo "An email has been sent to your address with a financial breakdown and recommendations!";

    $name = $_POST['name'];
    $email = $_POST['email'];
    $province = $_POST['province'];
    $income = $_POST['income'];
    $housingCosts = $_POST['housingCosts'];
    $groceries = $_POST['groceries'];
    $cellPhone = $_POST['cellPhone'];
    $children = $_POST['children'];
    $insurance = $_POST['insurance'];
    $liabilities = $_POST['liabilities'];
    $risk = 5;

    $my_array = $name .','. $email .','. $province .','. $income .','. $housingCosts .','. $groceries .','. $cellPhone .','. $children .','. $insurance .','. $liabilities .','. $risk ;
    //$risk = $_POST['risk'];
    //echo $my_array;
    
    //$result = shell_exec('C:\\Users\\graha\\AppData\\Local\\Microsoft\\WindowsApps\\python3.9.exe C:\\wamp64\\www\\FINANCE\\main.py ');
    $url = "http://localhost:5432/graham?arr=" . urlencode($my_array);

    $curl = curl_init($url);
    curl_setopt($curl, CURLOPT_HEADER, false);
    curl_setopt($curl, CURLOPT_RETURNTRANSFER, true);

    $json_response = curl_exec($curl);
    $status = curl_getinfo($curl, CURLINFO_HTTP_CODE);
    curl_close($curl);

    //echo $json_response;
  

    $insertRecordQuery = "INSERT INTO graham (nameDB, emailDB, provinceDB, incomeDB, housingCostsDB, groceriesDB, cellPhoneDB, childrenDB, insuranceDB, liabilitiesDB, riskDB) VALUES ($name, $email, $province, $income, $housingCosts, $groceries, $cellPhone, $children, $insurance, $liabilities, $risk)";
    /*
    if(mysqli_query($connection, $insertRecordQuery)){
        echo "Sucessfelly inserted <br>";
    } else {
        echo "Error in record insertion: ".mysqli_error($connection);
    }

    //Close connection
    $closeConnection = mysqli_close($connection);
    if($closeConnection){
        echo "Connection Closed :( <br>";
    } else {
        echo "Error closing connection <br>";
    }
    */

?>
