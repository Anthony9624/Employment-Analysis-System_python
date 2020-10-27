# 高校就业网爬虫&数据分析

## 站点功能
- 异步爬取湖南科技大学招聘网中的正式、实习职位& 校内、校外宣讲会& 湖南各地宣讲会
- 数据写入 MySql 和 ElasticSearch
- 使用 [elasticsearch-analysis-ik] 中文分词系统分词关键字
- 提供关键字搜索职位、宣讲会和宣讲会信息


## 详细介绍
爬虫通过修改数据获取接口 `count`参数控制爬取数量
```python
# 只爬取前两万条的岗位信息
for i in range(2):
    yield scrapy.Request("http://jy.hnust.edu.cn/module/getjobs?start_page=1&type_id=-1&k=&is_practice={0}&count=20000&start=1".format(i),
                         callback=self.handle_jobs)
```

## 界面
**搜索主页**
提供职位，宣讲会，双选会搜索和个人搜索记录
**图表页**
