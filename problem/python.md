how to create envs

    conda create -n larry python=3.6
    activate larry

 https://zhuanlan.zhihu.com/p/60647332

active in jupyter

    conda install nb_conda

   https://zhuanlan.zhihu.com/p/29564719

ValueError: check_hostname requires 
server_hostname

    close the proxy
    https://blog.csdn.net/bl_yang/article/details/116742097?spm=1001.2101.3001.6661.1&utm_medium=distribute.pc_relevant_t0.none-task-blog-2%7Edefault%7ECTRLIST%7Edefault-1.opensearchhbase&depth_1-utm_source=distribute.pc_relevant_t0.none-task-blog-2%7Edefault%7ECTRLIST%7Edefault-1.opensearchhbase

pip 2 slow:
    pip install django -i https://pypi.tuna.tsinghua.edu.cn/simple
    https://zhuanlan.zhihu.com/p/46975553

    import pkg_resources
    from subprocess import call
    
    for packages in [dist.project_name for dist in pkg_resources.working_set]:
        call("pip3 install --upgrade " + ''.join(packages) + ' --user' +'-i https://pypi.tuna.tsinghua.edu.cn/simple', shell=True)
        print(packages)


awesome package:
    https://github.com/huangboming/awesome-python

peak detection:
    https://stackoverflow.com/questions/1713335/peak-finding-algorithm-for-python-scipy

if __name__==__"main"__:
    https://cloud.tencent.com/developer/article/1538553

pandasGraph:
    https://pandas.liuzaoqi.com/intro.html

yield generator
    https://zhuanlan.zhihu.com/p/453927145  

python itself update
    https://blog.csdn.net/qq_43228739/article/details/108116208

conda update python
    https://blog.csdn.net/Defiler_Lee/article/details/109287412


pip list --outdated
pip-review --local  --interactive