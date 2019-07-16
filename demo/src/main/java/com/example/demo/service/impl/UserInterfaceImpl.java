package com.example.demo.service.impl;

import com.example.demo.service.UserInterface;
import com.example.demo.dao.UserDao;
import com.example.demo.entity.User;
import org.springframework.stereotype.Service;

import javax.annotation.Resource;
import java.util.List;

@Service
public class UserInterfaceImpl implements UserInterface {

    @Resource
    private UserDao userDao;

    @Override
    public List<User> getAllUser() {
        List<User> userList = userDao.getAllUser();
        return userList;
    }

    @Override
    public User getUserById(int userId) {
//        int a = 1/0;
        return userDao.getUserById(userId);
    }

    @Override
    public int insertUser(User user) {
        return userDao.insertUser(user);
    }

    @Override
    public int updataUser(User user) {
        return userDao.updataUser(user);
    }

    @Override
    public int deleteUser(int userId) {
        return userDao.deleteUser(userId);
    }
}
