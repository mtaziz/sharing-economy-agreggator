<?php
class App_View_Helper_HeadScript extends Zend_View_Helper_HeadScript {

    public function toString($indent = null) {
        /*
        * Add current script
        */
        $request = Zend_Controller_Front::getInstance()->getRequest();
        $module = $request->getModuleName();
        $controller = $request->getControllerName();

        $filePath		= '/js/' . $module . '/' . $controller . '.js';
        $modFilePath	= '/js/' . $module . '/mod.' . $module . '.js';

        $file		= PUBLIC_PATH . $filePath;
        $modFile	= PUBLIC_PATH . $modFilePath;

        if (file_exists($file)) {
            $url = $this->view->baseUrl() . $filePath;
            $this->appendFile($url);
        }

        if(file_exists($modFile)) {
            $url = $this->view->baseUrl() . $modFilePath;
            $this->appendFile($url);
        }

        // PARENT headScript function
        $indent = (null !== $indent)
            ? $this->getWhitespace($indent)
            : $this->getIndent();

        /*
        if ($this->view) {
            $useCdata = $this->view->doctype()->isXhtml() ? true : false;
        } else {
            $useCdata = $this->useCdata ? true : false;
        }
        $escapeStart = ($useCdata) ? '//<![CDATA[' : '//<!--';
        $escapeEnd   = ($useCdata) ? '//]]>'       : '//-->';
        */

        $escapeStart = '';
        $escapeEnd = '';

        $items = array();
        $this->getContainer()->ksort();
        foreach ($this as $item) {
            if (!$this->_isValid($item)) {
                continue;
            }

            $items[] = $this->itemToString($item, $indent, $escapeStart, $escapeEnd);
        }

        $return = implode($this->getSeparator(), $items);
        return $return;
    }
}