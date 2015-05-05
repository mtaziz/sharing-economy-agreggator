<?php
class App_Controller_Log
{

    const ACTION_HP      		= "home_page";
    const ACTION_result    	= "result_page";
    const ACTION_EXPORT    			= "";

    const SECTION_SEARCH      = "search";


    public static function logDb($typesection,$typeaction, $user_id=null, $params)
    {
        $modelLog = new Model_Log();
        $daoLog = new Dao_LogDao();

        $modelLog->section = $typesection;
        $modelLog->action = $typeaction;
        $modelLog->user_id = $user_id;
        $modelLog->ip = $_SERVER["REMOTE_ADDR"];
        $modelLog->variable = $params;
        
        $idLog = $daoLog->save($modelLog);
    }

}
