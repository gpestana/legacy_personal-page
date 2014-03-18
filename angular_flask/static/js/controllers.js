'use strict';

/* Controllers */

function IndexController($scope) {
	
}

function AboutController($scope) {
	
}

function PostListController($scope, Post) {
	var postsQuery = Post.get({}, function(posts) {
		$scope.posts = posts.objects;
	});
}

function PostDetailController($scope, $routeParams, Post) {
	var postQuery = Post.get({ postId: $routeParams.postId }, function(post) {
		$scope.post = post;
	});
}


function MessageController($scope, $routeParams, $http) {
	$http.get('http://localhost:5000/_api/message').
		success(function(data) {
			$scope.message = data;
			console.log(data);
		});
}
