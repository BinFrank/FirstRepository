package com.example.demo.controller;

import com.example.demo.entity.User;
import com.example.demo.service.UserInterface;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RestController;

import javax.annotation.Resource;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

@RestController
public class UserController {

    @Resource
    private UserInterface userInterface;

    @RequestMapping(value = "/listUser", method = RequestMethod.GET)
    private Map<String,Object> listUser(){
        Map<String,Object> modelMap = new HashMap<String, Object>();
        List<User> userList = userInterface.getAllUser();
        modelMap.put("userList", userList);
        return modelMap;
    }

    @RequestMapping(value = "/getUser", method = RequestMethod.GET)
    private Map<String, Object> getUserById(Integer userId){
        Map<String, Object> modelMap = new HashMap<String, Object>();
        User user = userInterface.getUserById(userId);
        modelMap.put("user", user);
        return modelMap;
    }

    @RequestMapping(value = "/addUser", method = RequestMethod.POST)
    private Map<String, Object> addUser(@RequestBody User user){
        Map<String, Object> modelMap = new HashMap<String, Object>();
        modelMap.put("success", userInterface.insertUser(user));
        return modelMap;
    }

    @RequestMapping(value = "/updataUser", method = RequestMethod.POST)
    private Map<String, Object> updateUser(@RequestBody User user){
        Map<String, Object> modelMap = new HashMap<String, Object>();
        modelMap.put("sussess", userInterface.updataUser(user));
        return modelMap;
    }

    @RequestMapping(value = "/deleteUser", method = RequestMethod.GET)
    private Map<String, Object> deleteUser(Integer userId){
        Map<String, Object> modelMap = new HashMap<String, Object>();
        modelMap.put("success", userInterface.deleteUser(userId));
        return modelMap;
    }
}
