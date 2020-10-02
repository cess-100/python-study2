"""
字典：
{
  '/index.py':index,
  '/center.py':center,
  '/gettime.py':gettime
}
"""
from application import funs

# 定义路由字典
route_dict = {
    '/index.py': funs.index,
    '/center.py': funs.center,
    '/gettime.py': funs.gettime
}
