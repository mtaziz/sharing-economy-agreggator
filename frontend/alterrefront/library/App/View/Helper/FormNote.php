<?php
require_once 'Zend/View/Helper/FormElement.php';


class App_View_Helper_FormNote extends Zend_View_Helper_FormElement {

    public function formNote($name, $value = null) {
        
        $info = $this->_getInfo($name, $value);
        extract($info); // name, value, attribs, options, listsep, disable
        return $value;
    }
}
