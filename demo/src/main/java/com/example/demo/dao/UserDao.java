package com.example.demo.dao;

import com.example.demo.entity.User;

import java.util.List;

public interface UserDao {
//    查询所有的用户
    List<User> getAllUser();

//    查询某个用户
    User getUserById(int userId);

//    添加用户
    int insertUser(User user);

//    修改用户信息
    int updataUser(User user);

//    删除用户
    int deleteUser(int userId);
}
