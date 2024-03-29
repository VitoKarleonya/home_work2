graph = {'0': set(['1', '2']),
'1': set(['0', '3', '4']),
'2': set(['0']),
'3': set(['1']),
'4': set(['2', '3'])}

def dfs(graph, start, visited = []):
	#здесь в аргументах сразу создается пустое множество и добавляется стартовая вершина 3
	visited.append(start)
	for v in graph[start]:
		#в цикле идет рекурсивный вызов функции dfs, в которой постоянно добавляется вершина, она меняется так как в нее подставлена v из цикла
		#потом когда цикл начинается заново оно добавляется в список и так пока будет что добавлять, в момент же когда цикл перебирая все значения  //
		# что все добавлено он вернет множетсво visited, если я чего то не учел пожалуйста скажите	
		if v not in visited:
			visited = dfs(graph, v, visited)
		return visited
print(dfs(graph, '3'))