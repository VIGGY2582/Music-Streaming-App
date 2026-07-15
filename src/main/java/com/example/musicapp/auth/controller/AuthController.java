package com.example.musicapp.auth.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import com.example.musicapp.auth.service.AuthService;
import com.example.musicapp.auth.dto.RegisterRequest;
import com.example.musicapp.auth.dto.LoginRequest;

@RestController
@RequestMapping("/auth")
public class AuthController {

    @Autowired
    private AuthService service;

    @PostMapping("/register")
    public String register(
            @RequestBody RegisterRequest request){

        return service.register(request);
    }

    @PostMapping("/login")
    public String login(
            @RequestBody LoginRequest request){

        return service.login(request);
    }
}