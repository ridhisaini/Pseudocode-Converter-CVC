package com.example.codak;

import android.annotation.SuppressLint;
import android.graphics.Color;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.view.WindowManager;
import android.widget.Button;
import android.widget.EditText;
import android.widget.LinearLayout;
import android.widget.TextView;
import android.widget.LinearLayout.LayoutParams;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.util.Scanner;

public class view_output extends AppCompatActivity
{
    TextView code , output;
    LinearLayout ll;
    LayoutParams lp;

    @Override
    protected void onCreate(Bundle savedInstanceState)
    {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_view_output);
        getWindow().addFlags(WindowManager.LayoutParams.FLAG_FULLSCREEN);
        code = (TextView) findViewById(R.id.code);
        output = (TextView) findViewById(R.id.output);
        File file = new File(CodakActivity.outputfile_path);
        try
        {
            code.setText(new Scanner(file).useDelimiter("\\Z").next());
        }
        catch (FileNotFoundException e)
        {
            e.printStackTrace();
        }
    }

    public void execute(View v)
    {
        output.setVisibility(View.VISIBLE);
    }
}
